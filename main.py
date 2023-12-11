import sys
import os
import subprocess
import functions
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
cwd = os.getcwd()


class anotherUI(QMainWindow):
    def __init__(self):
        super(anotherUI, self).__init__()
        loadUi('./gui/untitled.ui', self)

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('./gui/mainwin.ui', self)
        self.setWindowTitle('FMO Task Manager')
        self.one_btn.clicked.connect(self.one_btn_clicked)
        self.two_btn.clicked.connect(self.two_btn_clicked)
        self.three_btn.clicked.connect(self.show_anotherUI)

    def one_btn_clicked(self):
        subprocess.run(["xdg-open", "./tasks/tasks.md"])

    def two_btn_clicked(self):
        subprocess.run(["xdg-open", "./tasks/last_visited.md"])

    def show_anotherUI(self):
        self.window = anotherUI()
        self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    app.exec_()
