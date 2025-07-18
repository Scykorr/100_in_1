import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Учетные данные Yandex.Mail
login_main = 'inoutprojectsite@inoutproject.ru'  # Ваш логин (email) на Yandex.Mail
password = 'lxisjrjgvhagvqwb'  # Ваш пароль или пароль приложения

# Создаем объект сообщения
msg = MIMEMultipart()
msg['From'] = login_main
msg['To'] = 'fedosov-toxa@mail.ru'  # Email получателя
msg['Subject'] = 'Поздравляем! Вы успешно зарегистрировались на сайте inoutproject.ru!'

# HTML-контент
html_content = f"""
<html>
  <body>
    <h1>Поздравляем! Вы успешно зарегистрировались на сайте inoutproject.ru!</h1>
    <p>Ваши <b>логин и пароль</b> для доступа в клиентскую зону!</p>
    <ul>
      <li>Логин: {login_main}</li>
      <li>Пароль: {login_main}</li>
    </ul>
  </body>
</html>
"""

# Добавляем HTML-часть в сообщение
msg.attach(MIMEText(html_content, 'html', 'utf-8'))

# Отправка письма через Yandex.Mail
try:
    with smtplib.SMTP('smtp.yandex.ru', 587) as server:
        server.starttls()  # Включение шифрования TLS
        server.login(login_main, password)  # Авторизация
        server.sendmail(login_main, msg['To'], msg.as_string())  # Отправка письма
        print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")