import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
import tkinter as tk
from tkinter import messagebox, filedialog
import os


class FileRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Renamer")
        self.setGeometry(100, 100, 300, 150)

        self.label = QLabel("Enter new file name:", self)
        self.label.setGeometry(20, 20, 120, 20)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(150, 20, 120, 20)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(20, 60, 80, 30)
        self.browse_button.clicked.connect(self.browse_files)

        self.rename_button = QPushButton("Rename", self)
        self.rename_button.setGeometry(120, 60, 80, 30)
        self.rename_button.clicked.connect(self.rename_files)

        self.show()

    def browse_files(self):
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames()
        self.file_paths = list(file_paths)

    def rename_files(self):
        new_file_name = self.textbox.text().strip()
        if not new_file_name:
            messagebox.showerror("Error", "Please enter a new file name.")
            return

        for file_path in self.file_paths:
            directory = os.path.dirname(file_path)
            file_name, file_ext = os.path.splitext(os.path.basename(file_path))
            new_file_path = os.path.join(directory, file_name + file_ext)
            if new_file_path == file_path:
                messagebox.showinfo("Info", "The new file name is the same as the original name. No changes made.")
                continue
            if os.path.exists(new_file_path):
                messagebox.showerror("Error", f"A file with the name '{new_file_name + file_ext}' already exists.")
                continue
            try:
                os.rename(file_path, new_file_path)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                continue

            # Open the file in read mode
            with open('Paths.txt', 'r') as file:
                paths = file.readlines()

            # Remove the path from the list
            paths = [path for path in paths if path.strip() != file_path]

            # Open the file in write mode and write the updated paths
            with open('Paths.txt', 'w') as file:
                file.writelines(paths)

                # Save the path of the file in Paths.txt
                with open("Paths.txt", "a") as f:
                    f.write(new_file_path + "\n")

        messagebox.showinfo("Success", "Files renamed successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_renamer = FileRenamer()
    sys.exit(app.exec_())
