import sqlite3


class DiaryDb:
    def __init__(self):
        self.impulse()

    def impulse(self):
        self.conn_diary = sqlite3.connect('main_modules/diary_db.db')
        self.c = self.conn_diary.cursor()

    def task_select(self, true_id):
        if true_id:
            ret = []
            for id in true_id:
                self.c.execute(f'''SELECT id_task, name_task, rank_task, check_task FROM task WHERE id_task={id}''')
                ret += self.c.fetchall()
            return ret

    def date_select(self):
        self.c.execute('''SELECT id_task, start_date, end_date FROM task''')
        ret = self.c.fetchall()
        return ret

    def test_select(self):
        self.c.execute('''SELECT start_date, end_date FROM task''')
        ret = self.c.fetchall()
        return ret

        ############################################## from another project #######################################

    def get_org_by_id(self, id_org):
        self.c.execute('''SELECT * FROM organisation WHERE key_org = ? ''', (id_org,))
        ret = self.c.fetchall()
        return ret

    def deleteTcById(self, id_tc):
        self.c.execute('''DELETE FROM otss WHERE key_tc=(?)''', (id_tc,))
        self.conn_users.commit()

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
