
import sqlite3

class own:
    def __init__(self):
        self.impulse()
    def impulse(self):
        self.conn_users = sqlite3.connect('sssinfo.db')
        self.c = self.conn_users.cursor()

        self.create_user_db()

    def add_all_po(self, name, category):
        self.c.execute('''SELECT * FROM all_po WHERE name_all_po = ?''', (name,))
        ret = self.c.fetchall()
        if len(ret) == 0:
            self.c.execute('''
                       INSERT INTO all_po(name_all_po,category_all_po)
                       VALUES (?,?)''', (name, category,))
            self.conn_users.commit()

    def create_user_db(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "organisation" (
                "key_org"	INTEGER NOT NULL UNIQUE,
                "name_org"	TEXT,
                "small_name_org"	TEXT,
                "rank_rukow"	TEXT,
                "FIO_rukov"	TEXT,
                "adress_org"	TEXT,
                "vid_rab"	TEXT,
                "num_dogovor"	TEXT,
                "date_dogovor"	TEXT,
                "contact_phone"	TEXT,
                "summ_dogovor"	TEXT,
                "email"	TEXT,
                "inn_ogrn"	TEXT,
                "adress_urid" TEXT,
                PRIMARY KEY("key_org" AUTOINCREMENT)
               );''')
        self.conn_users.commit()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "tab_is" (
                "key_is"	INTEGER NOT NULL UNIQUE,
                "name_is"	TEXT,
                "adress_is"	TEXT,
                "vid_rabot"	TEXT,
                "type_is"	TEXT,
                "vid_is"	TEXT,
                "mashtab_is"	TEXT,
                "category_pdn"	TEXT,
                "volume_pdn"	TEXT,
                "otnosh_k_operatoru"	TEXT,
                "con_set_MIO"	TEXT,
                "rejim_obr"	TEXT,
                "prava_dost"	TEXT,
                "arch_is"	TEXT,
                "ur_znac_inf"	TEXT,
                "type_act_ugroz"	TEXT,
                "ur_zashish"	TEXT,
                "class_zashish"	TEXT,
                "date_rabot"	TEXT,
                "schema_is"	TEXT,
                "nazn_is"	TEXT,
                "kol_ARM"	TEXT,
                "kol_serv"	TEXT,
                "key_org"	TEXT,
                "obezlichivanie" TEXT,
                "int_s_drug_is" TEXT,
                PRIMARY KEY("key_is" AUTOINCREMENT)
            );''')
        self.conn_users.commit()

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS "pomesh" (
            "key_pomesh"	INTEGER NOT NULL UNIQUE,
            "name_pom"	TEXT,
            "numb_pom"	TEXT,
            "nazv_podrazd"	TEXT,
            "key_is"	INTEGER NOT NULL,
            "key_org"	INTEGER NOT NULL,
            PRIMARY KEY("key_pomesh" AUTOINCREMENT)
            );''')
        self.conn_users.commit()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS "dopushenye_k_ispdn" (
                "key_p"	INTEGER NOT NULL UNIQUE,
                "fio"	TEXT,
                "rank"	TEXT,
                "r_fio"   TEXT,
                "r_rank"  TEXT,
                "name_otd"	TEXT,
                "rol_k_ispdn"	TEXT,
                "ur_dost"	TEXT,
                "phone"	TEXT,
                "who_kommis"	TEXT,
                "name_kommis"	TEXT,
                "key_org"	INTEGER NOT NULL,
                "key_is"	INTEGER NOT NULL,
                PRIMARY KEY("key_p" AUTOINCREMENT)
             );''')
        self.conn_users.commit()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS "arm_otss" (
                "key_arm"    INTEGER NOT NULL UNIQUE,
                "name_arm"   TEXT,
                "set_name_arm"  TEXT,
                "model" TEXT,
                "serial_num"    TEXT,
                "mesto_ust" TEXT,
                "key_is"    INTEGER,
                PRIMARY KEY("key_arm" AUTOINCREMENT)
            );''')
        self.conn_users.commit()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS "otss" (
                "key_tc"	INTEGER NOT NULL UNIQUE,
                "name_tc"	TEXT,
                "model"	TEXT,
                "serial_num"	TEXT,
                "key_arm"	INTEGER,
                PRIMARY KEY("key_tc" AUTOINCREMENT)
            );''')
        self.conn_users.commit()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS "per_pdn" (
                    "key_pdn"	INTEGER NOT NULL UNIQUE,
                    "name_pdn"	INTEGER ,
                    "category_pdn"	TEXT,
                    "cel_obrabotki"	TEXT,
                    "osnovanie_obrabotki"	TEXT,
                    "kategory_sub_pdn"	TEXT,
                    "key_org"	INTEGER NOT NULL,
                    "key_is"	INTEGER NOT NULL,
                    PRIMARY KEY("key_pdn" AUTOINCREMENT)
                    );''')
        self.conn_users.commit()

        self.conn_users.execute('''
                CREATE TABLE IF NOT EXISTS "po_is" (
                    "key_po"	INTEGER NOT NULL UNIQUE,
                    "name_po"	TEXT,
                    "category_po"	TEXT,
                    "serial_numb_po"	TEXT,
                    "szz"	TEXT,
                    "vendor"	TEXT,
                    "numb_sertificate"	TEXT,
                    "time_deystv_sert"	TEXT,
                    "key_arm"	INTEGER,
                    PRIMARY KEY("key_po" AUTOINCREMENT)
                );''')
        self.conn_users.commit()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS "all_po" (
                    "key_all_po"	INTEGER NOT NULL UNIQUE,
                    "name_all_po"	TEXT NOT NULL,
                    "category_all_po"	TEXT NOT NULL,
                    PRIMARY KEY("key_all_po" AUTOINCREMENT)
                );''')
        self.conn_users.commit()