# This file contains all the classes for the GUI

# Normal imports
import os
import subprocess

# Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

# Variables
cwd = os.getcwd()
# New task window


class newTask(QMainWindow):
    def __init__(self):
        super(newTask, self).__init__()
        loadUi('./gui/newtask.ui', self)
        self.setWindowTitle('Add a new task')


# Our Last Visited file manager
class lastVisited(QMainWindow):
    def __init__(self):
        super(lastVisited, self).__init__()
        loadUi('./gui/fman.ui', self)
        self.browse.clicked.connect(self.browsefiles)
        self.ok_btn.clicked.connect(self.openfiles)
        self.setWindowTitle('Select Last Visited File')

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open File', cwd + '/tasks/last_visited')
        self.filename.setText(fname[0])

    def openfiles(self):
        text = self.filename.text()
        subprocess.run(["xdg-open", text])


# Our Pinned Tasks file manager
class pinnedTasks(QMainWindow):
    def __init__(self):
        super(pinnedTasks, self).__init__()
        loadUi('./gui/fman.ui', self)
        self.browse.clicked.connect(self.browsefiles)
        self.ok_btn.clicked.connect(self.openfiles)
        self.setWindowTitle('Select Pinned Tasks File')

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open File', cwd + '/tasks/pinned_tasks')
        self.filename.setText(fname[0])

    def openfiles(self):
        text = self.filename.text()
        subprocess.run(["xdg-open", text])
