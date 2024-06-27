import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from GUI import main_qt6
from main_modules import work_db_diary
import datetime
from main_modules import task_modul
from main_modules.tableModel import TableModel


class MyMainWindow(QMainWindow, main_qt6.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_diary = work_db_diary.DiaryDb()
        self.task_module = task_modul.TaskMod()

        self.calendarWidget.clicked.connect(self.calendar_click)
        self.show_data()

    def show_data(self) -> None:
        true_id: list = []
        current_date = self.calendarWidget.selectedDate()
        date_curr = current_date.toPyDate()
        if self.radioButton_tasks.isChecked():
            list_of_date = self.db_diary.date_select()
            for el in list_of_date:
                if datetime.date.fromisoformat(el[1]) <= date_curr <= datetime.date.fromisoformat(el[2]):
                    true_id.append(el[0])
            data, headers = self.task_module.task_select(true_id)
            self.update_table_view(data, headers)

    def calendar_click(self) -> None:
        self.show_data()

    def update_table_view(self, data: list, headers: list) -> None:
        if not data:
            data = ['']
        self.model = TableModel(data, headers)
        self.tableView_search_result.setModel(self.model)
        self.tableView_search_result.horizontalHeader().setStretchLastSection(True)
        self.tableView_search_result.setColumnHidden(0, 1)
        self.tableView_search_result.verticalHeader().setVisible(False)


def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    # main_window.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#
#         # Устанавливаем центральный виджет Window.
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         print("Clicked!")
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
