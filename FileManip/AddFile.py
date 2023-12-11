import os
import sys
import shutil

def add_file(file_name, path):

    if not os.path.exists(path):
        os.makedirs(path)
    shutil.copy(file_name, path)
