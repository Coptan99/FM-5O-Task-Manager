# Normal imports
import sys
import os
import subprocess

# Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

# Variables
cwd = os.getcwd()


# Our fancy UI
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi(cwd + '/gui/mainwin.ui', self)  # Load the .ui file
        self.setWindowTitle('FMO Task Manager')
        self.one_btn.clicked.connect(self.one_btn_clicked)
        self.two_btn.clicked.connect(self.two_btn_clicked)
        # self.three_btn.clicked.connect(self.show_anotherUI)

    def one_btn_clicked(self):
        subprocess.run(["xdg-open", "./tasks/tasks.md"])

    def two_btn_clicked(self):
        subprocess.run(["xdg-open", "./tasks/pinned.md"])


# Initialize the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    app.exec_()
