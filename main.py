# Normal imports
import sys

# Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

# Custom imports
from classes import *


# Our fancy UI
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('./gui/mainwin.ui', self)
        self.setWindowTitle('FMO Task Manager')

        # Defining functions for buttons
        self.zero_btn.clicked.connect(self.zero_btn_clicked)
        self.one_btn.clicked.connect(self.one_btn_clicked)
        self.two_btn.clicked.connect(self.two_btn_clicked)
        self.three_btn.clicked.connect(self.three_btn_clicked)
        self.four_btn.clicked.connect(self.four_btn_clicked)

    def zero_btn_clicked(self):
        self.file = newTask()
        self.file.show()

    def one_btn_clicked(self):
        self.file = lastVisited()
        self.file.show()

    def two_btn_clicked(self):
        self.file = pinnedTasks()
        self.file.show()

    def three_btn_clicked(self):
        pass

    def four_btn_clicked(self):
        pass


# Initialize the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    app.exec_()
