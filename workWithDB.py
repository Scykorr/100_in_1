import sqlite3


class Own:
    def __init__(self):
        self.impulse()

    def impulse(self):
        # таблица с администраторскими данными
        self.conn_admin = sqlite3.connect('admin.db')
        self.c_a = self.conn_admin.cursor()
        # тут таблица с данными организаций и ис
        self.conn_users = sqlite3.connect('sssinfo.db')
        self.c = self.conn_users.cursor()

        self.create_user_db()
        self.create_admin_db()

    def get_org_by_id(self, id_org):
        self.c.execute('''SELECT * FROM organisation WHERE key_org = ? ''', (id_org,))
        ret = self.c.fetchall()
        return ret

    def get_org_id_export(self, filepath_db):
        self.conn_users2 = sqlite3.connect(f'{filepath_db}')
        self.c2 = self.conn_users2.cursor()
        self.c2.execute('''SELECT key_org FROM organisation''')
        ret = self.c2.fetchall()
        return ret
    def drop_exist_db_export(self, filepath_db):
        self.conn_users2 = sqlite3.connect(f'{filepath_db}')
        self.c2 = self.conn_users2.cursor()
        self.c2.execute('''DELETE FROM organisation''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM all_po''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM arm_otss''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM dopushenye_k_ispdn''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM otss''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM per_pdn''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM po_is''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM pomesh''')
        self.conn_users2.commit()
        self.c2.execute('''DELETE FROM tab_is''')
        self.conn_users2.commit()



    def proof_is_name(self, name_is, key_org):
        self.c.execute('''SELECT * FROM tab_is WHERE name_is = ? AND key_org =? ''', (name_is, key_org))
        ret = self.c.fetchall()
        if len(ret) == 0:
            return 0
        else:
            return 1

    def add_new_is(self, idIs, name_is, adress_is, vid_rabot, type_is, vid_is, mashtab_is, category_pdn, volume_pdn,
                   otnosh_k_operatoru, con_set_MIO, regim_obr, prava_dost, arch_is, ur_znac_inf, type_act_ugroz,
                   ur_zashish_inf, class_zashish, date_rabot, schema_is, nazn_is, kol_ARM, kol_serv, key_org,
                   obezlichivanie, int_s_drug_is):
        self.c.execute('''SELECT * FROM tab_is WHERE key_is = ? AND key_org = ?''', (idIs, key_org))
        ret = self.c.fetchall()
        if len(ret) == 0:
            self.c.execute('''
                INSERT INTO tab_is(name_is,adress_is,vid_rabot,type_is,vid_is,mashtab_is,category_pdn,volume_pdn,
                                    otnosh_k_operatoru,con_set_MIO,rejim_obr,prava_dost,arch_is,ur_znac_inf,type_act_ugroz,
                                    ur_zashish,class_zashish,date_rabot,schema_is,nazn_is,kol_ARM,kol_serv,key_org,obezlichivanie,int_s_drug_is)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
                name_is, adress_is, vid_rabot, type_is, vid_is, mashtab_is, category_pdn, volume_pdn,
                otnosh_k_operatoru,
                con_set_MIO, regim_obr, prava_dost, arch_is, ur_znac_inf, type_act_ugroz, ur_zashish_inf, class_zashish,
                date_rabot, schema_is, nazn_is, kol_ARM, kol_serv, key_org, obezlichivanie, int_s_drug_is,))
            self.conn_users.commit()
            return 1
        else:
            self.c.execute('''
                UPDATE tab_is
                SET name_is=?,adress_is=?,vid_rabot=?,type_is=?,vid_is=?,mashtab_is=?,category_pdn=?,volume_pdn=?,
                    otnosh_k_operatoru=?,con_set_MIO=?,rejim_obr=?,prava_dost=?,arch_is=?,ur_znac_inf=?,type_act_ugroz=?,
                    ur_zashish=?,class_zashish=?,date_rabot=?,nazn_is=?,kol_ARM=?,kol_serv=?,obezlichivanie=?,int_s_drug_is=?
                WHERE key_is = ? 
               ''', (
                name_is, adress_is, vid_rabot, type_is, vid_is, mashtab_is, category_pdn, volume_pdn,
                otnosh_k_operatoru,
                con_set_MIO, regim_obr, prava_dost, arch_is, ur_znac_inf, type_act_ugroz, ur_zashish_inf, class_zashish,
                date_rabot, nazn_is, kol_ARM, kol_serv, obezlichivanie, int_s_drug_is, ret[0][0],))
            self.conn_users.commit()
            return 2

    def update_tab_is_schema(self, schema, id_is):
        self.c.execute('''
                        UPDATE tab_is
                        SET schema_is=?
                        WHERE key_is = ? 
                       ''', (
            schema, id_is,))
        self.conn_users.commit()

    def delete_org(self, id_org):
        self.c.execute('''DELETE FROM organisation WHERE key_org=(?)''', (id_org,))
        self.conn_users.commit()

        informationSystem = self.get_all_is(id_org)
        for i in range(0, len(informationSystem)):
            self.delete_is(informationSystem[i][0])

    def delete_is(self, id_is):
        self.c.execute('''DELETE FROM tab_is WHERE key_is=(?)''', (id_is,))
        self.conn_users.commit()

        arm = self.get_all_arm(id_is)
        for i in range(0, len(arm)):
            self.delete_arm(arm[i][0])

        per_pdn = self.get_per_pdn(id_is)
        for i in range(0, len(per_pdn)):
            self.delete_pdn(per_pdn[i][0])

    def get_all_arm(self, id_is):
        self.c.execute('''SELECT * FROM arm_otss WHERE key_is = ?''', (id_is,))
        ret = self.c.fetchall()
        return ret

    def get_schema(self, id_is):
        self.c.execute('''SELECT schema_is FROM tab_is WHERE key_is = ?''', (id_is,))
        ret = self.c.fetchall()
        return ret

    def get_all_is(self, id_org):
        self.c.execute('''SELECT key_is FROM tab_is WHERE key_org = ?''', (id_org,))
        ret = self.c.fetchall()
        return ret

    def get_select_arm(self, idArmOtss):
        self.c.execute('''SELECT * FROM arm_otss WHERE key_arm = ?''', (idArmOtss,))
        ret = self.c.fetchall()
        return ret

    def delete_arm(self, id_arm):
        self.c.execute('''DELETE FROM arm_otss WHERE key_arm=(?)''', (id_arm,))
        self.conn_users.commit()

        tc = self.get_all_tc(id_arm)
        for i in range(0, len(tc)):
            self.deleteTcById(tc[i][0])

        po = self.get_po(id_arm)
        for i in range(0, len(po)):
            self.delete_po(po[i][0])

    def save_arm(self, name_arm, set_name_arm, model, serial_numb, mesto_ust, key_is, key_arm):
        self.c.execute('''SELECT * FROM arm_otss WHERE key_arm = ? AND key_is = ? ''', (key_arm, key_is))
        ret = self.c.fetchall()

        if len(ret) == 0:
            self.c.execute('''
                INSERT INTO arm_otss(name_arm,set_name_arm,model,serial_num,mesto_ust,key_is)
                VALUES (?,?,?,?,?,?)''', (name_arm, set_name_arm, model, serial_numb, mesto_ust, key_is,))
            self.conn_users.commit()
            return 1
        else:
            key_arm = ret[0][0]
            self.c.execute('''
               UPDATE arm_otss
               SET name_arm=?,set_name_arm=?,model=?,serial_num=?,mesto_ust=?
               WHERE key_arm = ? 
               ''', (name_arm, set_name_arm, model, serial_numb, mesto_ust, key_arm,))
            self.conn_users.commit()
            return 2

    def get_all_tc(self, id_arm):
        self.c.execute('''SELECT * FROM otss WHERE key_arm = ?''', (id_arm,))
        ret = self.c.fetchall()
        return ret

    def getTcById(self, idTc):
        self.c.execute('''SELECT * FROM otss WHERE key_tc = ?''', (idTc,))
        ret = self.c.fetchall()
        return ret

    def get_select_tc(self, idOtssTs):
        self.c.execute('''SELECT * FROM otss WHERE key_tc = ?''', (idOtssTs,))
        ret = self.c.fetchall()
        return ret

    def save_tc(self, name_tc, model, serial_numb, key_arm, key_tc):
        self.c.execute('''SELECT * FROM otss WHERE key_tc = ? AND key_arm = ? ''', (key_tc, key_arm))
        ret = self.c.fetchall()

        if len(ret) == 0:
            self.c.execute('''
                INSERT INTO otss(name_tc,model,serial_num,key_arm)
                VALUES (?,?,?,?)''', (name_tc, model, serial_numb, key_arm,))
            self.conn_users.commit()
            return 1
        else:
            key_tc = ret[0][0]
            self.c.execute('''
               UPDATE otss
               SET name_tc=?,model=?,serial_num=?
               WHERE key_tc = ? 
               ''', (name_tc, model, serial_numb, key_tc,))
            self.conn_users.commit()
            return 2

    def deleteTcById(self, id_tc):
        self.c.execute('''DELETE FROM otss WHERE key_tc=(?)''', (id_tc,))
        self.conn_users.commit()

    def delete_tc(self, idOtssTs):
        self.c.execute('''DELETE FROM otss WHERE key_tc=(?)''', (idOtssTs,))
        self.conn_users.commit()

    def get_pomesh(self, id_is):
        self.c.execute('''SELECT * FROM pomesh WHERE key_is = ?''', (id_is,))
        ret = self.c.fetchall()
        return ret

    def get_select_pomesh(self, id_pm):
        self.c.execute('''SELECT * FROM pomesh WHERE key_pomesh = ?''', (id_pm,))
        ret = self.c.fetchall()
        return ret

    def add_pomesheniya(self, name, number, name_otd, id_is, id_org, idPomesh):
        if idPomesh == "":
            ret = ()
        else:
            self.c.execute('''SELECT * FROM pomesh WHERE key_is = ? AND key_pomesh = ?''', (id_is, idPomesh))
            ret = self.c.fetchall()

        if len(ret) == 0:
            self.c.execute('''
                INSERT INTO pomesh(name_pom,numb_pom,nazv_podrazd,key_is,key_org)
                VALUES (?,?,?,?,?)''', (name, number, name_otd, id_is, id_org,))
            self.conn_users.commit()
            return 1
        else:
            key_pm = ret[0][0]
            self.c.execute('''
               UPDATE pomesh
               SET name_pom=?,numb_pom=?,nazv_podrazd=?,key_is=?,key_org=?
               WHERE key_pomesh = ? 
               ''', (name, number, name_otd, id_is, id_org, idPomesh,))
            self.conn_users.commit()
            return 2

    def delete_pomeseniya(self, id_pm):
        self.c.execute('''DELETE FROM pomesh WHERE key_pomesh=(?)''', (id_pm,))
        self.conn_users.commit()

    def get_per_pdn(self, id_is):
        self.c.execute('''SELECT * FROM per_pdn WHERE key_is = ?''', (id_is,))
        ret = self.c.fetchall()
        return ret

    def get_select_pdn(self, id_pdn):
        self.c.execute('''SELECT * FROM per_pdn WHERE key_pdn = ?''', (id_pdn,))
        ret = self.c.fetchall()
        return ret

    def save_pdn(self, name_pdn, category_pdn, cel_obrabotki, osnov_obrab, categ_sub, id_org, id_is, idPdn):
        if idPdn == "":
            ret = ()
        else:
            self.c.execute('''SELECT * FROM per_pdn WHERE key_pdn = ? AND key_is = ? ''', (idPdn, id_is,))
            ret = self.c.fetchall()

        if len(ret) == 0:
            self.c.execute('''
                INSERT INTO per_pdn(name_pdn,category_pdn,cel_obrabotki,osnovanie_obrabotki,kategory_sub_pdn,key_org,key_is)
                VALUES (?,?,?,?,?,?,?)''',
                           (name_pdn, category_pdn, cel_obrabotki, osnov_obrab, categ_sub, id_org, id_is,))
            self.conn_users.commit()
            return 1
        else:
            key_pdn = ret[0][0]
            self.c.execute('''
               UPDATE per_pdn
               SET name_pdn=?,category_pdn=?,cel_obrabotki=?,osnovanie_obrabotki=?,kategory_sub_pdn=?
               WHERE key_pdn = ? 
               ''', (name_pdn, category_pdn, cel_obrabotki, osnov_obrab, categ_sub, key_pdn,))
            self.conn_users.commit()
            return 2

    def delete_pdn(self, id_pdn):
        self.c.execute('''DELETE FROM per_pdn WHERE key_pdn=(?)''', (id_pdn,))
        self.conn_users.commit()

    def get_select_org(self, id_org):
        self.c.execute('''SELECT * FROM organisation WHERE key_org = ?''', (id_org,))
        ret = self.c.fetchall()
        return ret

    def add_all_po(self, name, category):
        self.c.execute('''SELECT * FROM all_po WHERE name_all_po = ?''', (name,))
        ret = self.c.fetchall()
        if len(ret) == 0:
            self.c.execute('''
                    INSERT INTO all_po(name_all_po,category_all_po)
                    VALUES (?,?)''', (name, category,))
            self.conn_users.commit()

    def get_all_po_name(self):
        self.c.execute('''SELECT * FROM all_po''')
        ret = self.c.fetchall()
        return ret

    def add_po(self, name, category, serial_numb, num_sert, szz, time_deyst, id_arm, idOtssPo):
        self.add_all_po(name, category)

        self.c.execute('''SELECT * FROM po_is WHERE key_po = ? and key_arm = ?''', (idOtssPo, id_arm))
        ret = self.c.fetchall()
        if len(ret) == 0:
            self.c.execute('''
                    INSERT INTO po_is(name_po,category_po,serial_numb_po,szz,numb_sertificate,time_deystv_sert,key_arm)
                    VALUES (?,?,?,?,?,?,?)''', (name, category, serial_numb, szz, num_sert, time_deyst, id_arm,))
            self.conn_users.commit()
            return 1

        else:
            id_po = ret[0][0]
            self.c.execute('''
               UPDATE po_is
               SET name_po=?,category_po=?,serial_numb_po=?,szz=?,numb_sertificate=?,time_deystv_sert=?
               WHERE key_po = ? 
               ''', (name, category, serial_numb, szz, num_sert, time_deyst, id_po,))
            self.conn_users.commit()
            return 2

    def get_select_po(self, idOtssPo):
        self.c.execute('''SELECT * FROM po_is WHERE key_po = ?''', (idOtssPo,))
        ret = self.c.fetchall()
        return ret

    def get_po(self, id_arm):
        self.c.execute('''SELECT * FROM po_is WHERE key_arm = ?''', (id_arm,))
        ret = self.c.fetchall()
        return ret

    def deletePoById(self, id_po):
        self.c.execute('''DELETE FROM po_is WHERE key_po=(?)''', (id_po,))
        self.conn_users.commit()

    def delete_po(self, idOtssPo):
        self.c.execute('''DELETE FROM po_is WHERE key_po=(?)''', (idOtssPo,))
        self.conn_users.commit()

    def get_dopush(self, id_is):
        self.c.execute('''SELECT * FROM dopushenye_k_ispdn WHERE key_is = ?''', (id_is,))
        ret = self.c.fetchall()
        return ret

    def get_select_dopush(self, id_d):
        self.c.execute('''SELECT * FROM dopushenye_k_ispdn WHERE key_p = ?''', (id_d,))
        ret = self.c.fetchall()
        return ret

    def add_dopush(self, fio, dolg, fio_r, dolg_r, name_otd, rol_k_ispdn, ur_dost, phone, who_kom, name_kom, id_is,
                   id_org, idDopush):
        if idDopush == "":
            ret = ()
        else:
            self.c.execute('''SELECT * FROM dopushenye_k_ispdn WHERE key_p = ?''', (idDopush,))
            ret = self.c.fetchall()
        if len(ret) == 0:
            self.c.execute('''
                                INSERT INTO dopushenye_k_ispdn(fio,rank,r_fio,r_rank,name_otd,rol_k_ispdn,ur_dost,phone,who_kommis,name_kommis,key_is,key_org)
                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (
                fio, dolg, fio_r, dolg_r, name_otd, rol_k_ispdn, ur_dost, phone, who_kom, name_kom, id_is, id_org,))
            self.conn_users.commit()
            return 1

        else:
            self.c.execute('''
                       UPDATE dopushenye_k_ispdn
                       SET fio=?, rank=?, r_fio=?, r_rank=?, name_otd=?, rol_k_ispdn=?, ur_dost=?, phone=?, who_kommis=?, name_kommis=?, key_is=?, key_org=?
                       WHERE key_p = ? 
                       ''', (
                fio, dolg, fio_r, dolg_r, name_otd, rol_k_ispdn, ur_dost, phone, who_kom, name_kom, id_is, id_org,
                idDopush))
            self.conn_users.commit()
            return 2

    def delete_dopush(self, id_d):
        self.c.execute('''DELETE FROM dopushenye_k_ispdn WHERE key_p=(?)''', (id_d,))
        self.conn_users.commit()

    def get_all_org(self):
        self.c.execute('''SELECT * FROM organisation''')
        ret = self.c.fetchall()
        return ret

    def get_all_num_dogovor(self):
        self.c.execute('''SELECT num_dogovor FROM organisation''')
        ret = self.c.fetchall()
        return ret

    def get_select_is(self, id_is):
        self.c.execute('''SELECT * FROM tab_is WHERE key_is = ? ''', (id_is,))
        ret = self.c.fetchall()
        return ret[0]

    def get_is_org(self, id_org):
        self.c.execute('''SELECT * FROM tab_is WHERE key_org = ? ''', (id_org,))
        ret = self.c.fetchall()
        return ret

    def add_organisation(self, name_org, small_name_org, fio_rukow, dolg_rukow, adres_org, vid_rabot, date_zak_dogovora,
                         inn_ogrn, numb_dog_rab, contact_phone, email, summ_dog, adress_urid):
        self.c.execute('''SELECT * FROM organisation WHERE num_dogovor = ? ''', (numb_dog_rab,))
        ret = self.c.fetchall()

        if len(ret) == 0:
            self.c.execute('''
            INSERT INTO organisation(name_org,small_name_org,rank_rukow,FIO_rukov,adress_org,vid_rab,num_dogovor,date_dogovor,contact_phone,summ_dogovor,email,inn_ogrn,adress_urid)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
                name_org, small_name_org, dolg_rukow, fio_rukow, adres_org, vid_rabot, numb_dog_rab, date_zak_dogovora,
                contact_phone, summ_dog, email, inn_ogrn, adress_urid,))
            self.conn_users.commit()
            self.c.execute('''SELECT key_org FROM organisation WHERE num_dogovor = ? ''', (numb_dog_rab,))
            ret_o = self.c.fetchall()

            return ret_o[0][0]
        else:
            return 0

    def change_organisation(self, id_org, name_org, small_name_org, fio_rukow, dolg_rukow, adres_org, vid_rabot,
                            date_zak_dogovora, inn_ogrn, numb_dog_rab, contact_phone, email, summ_dog, adress_urid):
        self.c.execute('''SELECT * FROM organisation WHERE num_dogovor = ? ''', (numb_dog_rab,))
        ret = self.c.fetchall()
        if len(ret) == 0:
            ret = [[id_org]]
        if int(ret[0][0]) == int(id_org):
            self.c.execute('''
            UPDATE organisation
            SET name_org=?,small_name_org=?,rank_rukow=?,FIO_rukov=?,adress_org=?,vid_rab=?,num_dogovor=?,date_dogovor=?,contact_phone=?,summ_dogovor=?,email=?,inn_ogrn=?,adress_urid=?
            WHERE key_org = ?
            ''', (
                name_org, small_name_org, dolg_rukow, fio_rukow, adres_org, vid_rabot, numb_dog_rab, date_zak_dogovora,
                contact_phone, summ_dog, email, inn_ogrn, adress_urid, id_org,))
            self.conn_users.commit()
            self.c.execute('''SELECT key_org FROM organisation WHERE num_dogovor = ? ''', (numb_dog_rab,))
            ret_o = self.c.fetchall()

            return ret_o[0][0]
        else:
            return 0

    def get_tab_is_vsdx_blob(self, id_tab_is):
        self.c.execute('''SELECT name_is, schema_is from tab_is WHERE key_is = {0}'''.format(
            id_tab_is
        ))
        ret = self.c.fetchall()
        return ret

    def proof_aut(self, login, password):
        self.c_a.execute('''SELECT * FROM users WHERE login =(?) AND password =(?) ''', (login, password,))
        ret = self.c_a.fetchall()

        if len(ret) == 0:
            return 0
        else:
            return ret[0][3]

    def get_org_num_dogovor(self):
        self.c.execute('''SELECT num_dogovor from organisation''')
        ret = self.c.fetchall()
        return ret

    def create_admin_db(self):
        self.c_a.execute('''
        CREATE TABLE IF NOT EXISTS "users" (
	   "id"	INTEGER NOT NULL UNIQUE,
	   "login"	TEXT,
	   "password" TEXT,
	   "access" TEXT,
	   PRIMARY KEY("id" AUTOINCREMENT)
	   );''')
        self.conn_admin.commit()

        self.c_a.execute('''SELECT * FROM users''')
        ret = self.c_a.fetchall()
        if len(ret) == 0:
            self.c_a.execute('''
                INSERT INTO users(login,password,access) VALUES ('a','a','admin')''')
            self.conn_admin.commit()
            self.c_a.execute('''
                INSERT INTO users(login,password,access) VALUES ('user','user','user')''')
            self.conn_admin.commit()

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
        	"schema_is"	BLOB,
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
