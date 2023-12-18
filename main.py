# Normal imports
import sys
import os
import subprocess

# Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5.uic import loadUi

# Variables
cwd = os.getcwd()
file = cwd + '/tasks/task.txt'

class Fman(QMainWindow):
    def __init__(self):
        super(Fman, self).__init__()
        loadUi('./gui/fman.ui', self)
        self.browse.clicked.connect(self.browsefiles)
        
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', cwd + '/tasks')
        self.filename.setText(fname[0])
        

# Our fancy UI
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('./gui/mainwin.ui', self)
        self.setWindowTitle('FMO Task Manager')
        
        # Defining functions for buttons
        self.one_btn.clicked.connect(self.one_btn_clicked)
        self.two_btn.clicked.connect(self.two_btn_clicked)

    def one_btn_clicked(self):
        self.file = Fman()
        self.file.show()

    def two_btn_clicked(self):
        subprocess.run(["xdg-open", "./tasks/last_visited.md"])


# Initialize the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    app.exec_()
