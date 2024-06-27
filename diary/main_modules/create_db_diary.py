import sqlite3


class own:
    def __init__(self):
        self.impulse()

    def impulse(self):
        self.conn_diary = sqlite3.connect('diary_db.db')
        self.c = self.conn_diary.cursor()

        self.create_diary_db()

    def create_diary_db(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "task" (
                "id_task"	INTEGER NOT NULL UNIQUE,
                "name_task"	TEXT,
                "name_description"	TEXT,
                "rank_task"	INTEGER,
                "check_task" INTEGER,
                PRIMARY KEY("id_task" AUTOINCREMENT)
               );''')
        self.conn_diary.commit()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "human" (
                "id_human"	INTEGER NOT NULL UNIQUE,
                "name_human"	TEXT,
                "surname_human"	TEXT,
                "fathers_name_human" TEXT,
                "human_description" TEXT,
                "birthday_date"	DATETIME,
                "telephone_num"	TEXT,
                "human_group"	TEXT,
                PRIMARY KEY("id_human" AUTOINCREMENT)
            );''')
        self.conn_diary.commit()


a = own().create_diary_db()

