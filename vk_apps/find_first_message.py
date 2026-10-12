#!/usr/bin/env python3
"""
Найти в беседе VK:
  1) когда пользователь впервые появился (invite / join action);
  2) когда он написал первое обычное сообщение.

По умолчанию — id37861441 в беседе peer_id=2000000065.

Нужен пользовательский access_token с правом messages.
Без токена API недоступен — см. README.md.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # optional
    def load_dotenv() -> bool:  # type: ignore[misc]
        return False

import requests

DEFAULT_USER_ID = 37861441
DEFAULT_PEER_ID = 2000000065  # https://vk.ru/im/convo/2000000065
API_URL = "https://api.vk.com/method/messages.getHistory"
JOIN_ACTIONS = {
    "chat_invite_user",
    "chat_invite_user_by_link",
    "chat_invite_user_by_call",
    "chat_invite_user_by_message_request",
    "chat_create",
}


def ts_to_str(unix_ts: int) -> str:
    return datetime.fromtimestamp(unix_ts, tz=timezone.utc).astimezone().strftime(
        "%Y-%m-%d %H:%M:%S %Z"
    )


def vk_call(
    token: str,
    api_version: str,
    peer_id: int,
    *,
    offset: int,
    count: int,
    rev: int,
    session: requests.Session,
) -> dict[str, Any]:
    params = {
        "access_token": token,
        "v": api_version,
        "peer_id": peer_id,
        "offset": offset,
        "count": count,
        "rev": rev,
        "extended": 0,
    }
    resp = session.get(API_URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        err = data["error"]
        raise RuntimeError(
            f"VK API error {err.get('error_code')}: {err.get('error_msg')}"
        )
    return data["response"]


def message_preview(msg: dict[str, Any], limit: int = 120) -> str:
    text = (msg.get("text") or "").replace("\n", " ").strip()
    action = msg.get("action") or {}
    if action:
        kind = action.get("type", "?")
        member = action.get("member_id")
        extra = f", member_id={member}" if member is not None else ""
        base = f"[action:{kind}{extra}]"
        return f"{base} {text}".strip()[:limit]
    return text[:limit] if text else "[без текста / вложение]"


def is_join_for_user(msg: dict[str, Any], user_id: int) -> bool:
    action = msg.get("action") or {}
    if not action:
        return False
    kind = action.get("type")
    if kind not in JOIN_ACTIONS:
        return False
    member_id = action.get("member_id")
    if member_id is not None:
        return int(member_id) == user_id
    # chat_create / редкие кейсы без member_id — считаем join, если from_id = user
    return int(msg.get("from_id") or 0) == user_id


def is_user_text_message(msg: dict[str, Any], user_id: int) -> bool:
    if int(msg.get("from_id") or 0) != user_id:
        return False
    if msg.get("action"):
        return False
    return True


def scan_history(
    token: str,
    api_version: str,
    peer_id: int,
    user_id: int,
    *,
    batch: int,
    sleep_s: float,
    max_messages: int | None,
) -> dict[str, Any]:
    session = requests.Session()
    offset = 0
    scanned = 0
    total: int | None = None
    first_join: dict[str, Any] | None = None
    first_message: dict[str, Any] | None = None

    while True:
        if max_messages is not None and scanned >= max_messages:
            break
        count = batch
        if max_messages is not None:
            count = min(batch, max_messages - scanned)

        response = vk_call(
            token,
            api_version,
            peer_id,
            offset=offset,
            count=count,
            rev=1,  # от старых к новым
            session=session,
        )
        if total is None:
            total = int(response.get("count") or 0)
            print(f"Всего сообщений в беседе (по API): {total}", file=sys.stderr)

        items = response.get("items") or []
        if not items:
            break

        for msg in items:
            scanned += 1
            if first_join is None and is_join_for_user(msg, user_id):
                first_join = msg
                print(
                    f"Найден вход/приглашение: id={msg.get('id')} "
                    f"date={ts_to_str(int(msg['date']))}",
                    file=sys.stderr,
                )
            if first_message is None and is_user_text_message(msg, user_id):
                first_message = msg
                print(
                    f"Найдено первое сообщение: id={msg.get('id')} "
                    f"date={ts_to_str(int(msg['date']))}",
                    file=sys.stderr,
                )
            if first_join is not None and first_message is not None:
                return {
                    "total_in_chat": total,
                    "scanned": scanned,
                    "first_join": first_join,
                    "first_message": first_message,
                    "complete": True,
                }

        offset += len(items)
        if offset >= (total or 0) or len(items) < count:
            break
        if sleep_s > 0:
            time.sleep(sleep_s)

    return {
        "total_in_chat": total,
        "scanned": scanned,
        "first_join": first_join,
        "first_message": first_message,
        "complete": first_join is not None and first_message is not None,
    }


def summarize_hit(label: str, msg: dict[str, Any] | None) -> dict[str, Any]:
    if msg is None:
        return {"found": False, "label": label}
    return {
        "found": True,
        "label": label,
        "message_id": msg.get("id"),
        "date_unix": msg.get("date"),
        "date_local": ts_to_str(int(msg["date"])),
        "from_id": msg.get("from_id"),
        "conversation_message_id": msg.get("conversation_message_id"),
        "preview": message_preview(msg),
        "action": msg.get("action"),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Найти первое появление и первое сообщение пользователя в беседе VK"
        )
    )
    p.add_argument(
        "--user-id",
        type=int,
        default=DEFAULT_USER_ID,
        help=f"ID пользователя (по умолчанию {DEFAULT_USER_ID})",
    )
    p.add_argument(
        "--peer-id",
        type=int,
        default=DEFAULT_PEER_ID,
        help=f"peer_id беседы (по умолчанию {DEFAULT_PEER_ID})",
    )
    p.add_argument(
        "--token",
        default=None,
        help="access_token (иначе VK_ACCESS_TOKEN из env / .env)",
    )
    p.add_argument(
        "--api-version",
        default=None,
        help="версия API (иначе VK_API_VERSION или 5.199)",
    )
    p.add_argument("--batch", type=int, default=200, help="размер страницы (≤200)")
    p.add_argument(
        "--sleep",
        type=float,
        default=0.35,
        help="пауза между запросами, сек (антифлуд)",
    )
    p.add_argument(
        "--max-messages",
        type=int,
        default=None,
        help="ограничить сканирование N самыми старыми сообщениями",
    )
    p.add_argument(
        "--json-out",
        default=None,
        help="путь для полного JSON-отчёта",
    )
    return p.parse_args()


def main() -> int:
    load_dotenv()
    args = parse_args()
    token = args.token or os.getenv("VK_ACCESS_TOKEN") or os.getenv("VK_TOKEN")
    api_version = (
        args.api_version or os.getenv("VK_API_VERSION") or "5.199"
    )
    batch = max(1, min(200, args.batch))

    if not token:
        print(
            "Нет access_token.\n"
            "Положите VK_ACCESS_TOKEN в vk_apps/.env или передайте --token.\n"
            "Автоматически без регистрации приложения / токена это сделать нельзя.\n"
            "Подробности: vk_apps/README.md",
            file=sys.stderr,
        )
        return 2

    print(
        f"Ищем user_id={args.user_id} в peer_id={args.peer_id} "
        f"(от самых старых сообщений)...",
        file=sys.stderr,
    )
    try:
        result = scan_history(
            token,
            api_version,
            args.peer_id,
            args.user_id,
            batch=batch,
            sleep_s=args.sleep,
            max_messages=args.max_messages,
        )
    except Exception as exc:  # noqa: BLE001 — CLI
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1

    report = {
        "user_id": args.user_id,
        "peer_id": args.peer_id,
        "user_url": f"https://vk.ru/id{args.user_id}",
        "convo_url": f"https://vk.ru/im/convo/{args.peer_id}",
        "total_in_chat": result["total_in_chat"],
        "scanned": result["scanned"],
        "complete": result["complete"],
        "first_join": summarize_hit("first_join_or_invite", result["first_join"]),
        "first_message": summarize_hit(
            "first_user_message", result["first_message"]
        ),
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Отчёт сохранён: {args.json_out}", file=sys.stderr)

    if not result["complete"]:
        print(
            "Не всё найдено: пользователя могли добавить без action-сообщения "
            "в доступной истории, или история обрезана / нет прав.",
            file=sys.stderr,
        )
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
