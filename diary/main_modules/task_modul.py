from diary.main_modules import work_db_diary
import datetime
import time


class TaskMod:

    def __init__(self):
        self.db_diary = work_db_diary.DiaryDb()

    def task_select(self, true_id):
        test_select = list(map(list, self.db_diary.task_select(true_id)))
        headers = ['id_task', 'Задача', 'Ранг', 'Статус']
        return test_select, headers

# currDate = datetime.date.today()
#         self.dateEdit_date_zak_dogovora.setDate(QtCore.QDate(currDate.year, currDate.month, currDate.day))


#
# ret = Own().get_all_org()
#             data = []
#             for i in range(len(ret)):
#                 if input_text.lower() in str(ret[i][2]).lower():
#                     data.append([str(ret[i][0]), str(ret[i][2]), str(ret[i][7]), str(ret[i][8])])
#
#             if data == []:
#                 data = ['']
#                 headers = ['id TC', 'Организация', '№ договора', 'Дата проведения\n работ']
#                 self.model = TableModel(data, headers)
#                 self.ui.tableViewOrg.setModel(self.model)
#                 self.ui.tableViewOrg.horizontalHeader().setStretchLastSection(True)
#                 self.ui.tableViewOrg.setColumnHidden(0, 1)
#                 self.ui.tableViewOrg.verticalHeader().setVisible(False)
