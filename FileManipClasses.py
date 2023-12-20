# This file contains all the classes for the GUI

# Normal imports
import os
import subprocess
from FileManip import AddVault

# Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

class NewVault(QMainWindow):
    def __init__(self):
        super(NewVault, self).__init__()
        loadUi("./gui/AddVault.ui", self)
        self.setWindowTitle("New Vault")
        self.setFixedSize(self.size())
        self.show()

        self.ChooseButton.clicked.connect(self.browse)
        self.OkButton.clicked.connect(self.create)


