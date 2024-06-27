import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from GUI import main

class MyMainWindow(QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    #main_window.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
