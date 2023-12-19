import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def get_file_paths(file_path):
    file_paths = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("File path:"):
                file_paths.append(line.strip().split(": ")[1])
    return file_paths

def choose_file_from_list(file_paths):
    root = tk.Tk()
    root.withdraw()
    chosen_file_path = simpledialog.askstring("Select File", "Choose a file:",
                                              parent=root,
                                              initialvalue=file_paths[0])
    if chosen_file_path is None:
        return None

    return chosen_file_path

def open_file_in_default_editor(file_path):
    if os.name == "nt":  # Windows
        os.startfile(file_path)
    elif os.name == "posix":  # Linux or macOS
        os.system(f"open {file_path}")
    else:
        raise OSError("Unsupported operating system.")

# Path to the "Paths.txt" file
file_path = "Paths.txt"

# Get the file paths from the file
file_paths = get_file_paths(file_path)

# Choose a file from the list
chosen_file = choose_file_from_list(file_paths)

# Display the chosen file
if chosen_file:
    messagebox.showinfo("Chosen File", f"You chose: {chosen_file}")

    try:
        # Open the file in the default editor
        open_file_in_default_editor(chosen_file)
    except OSError as e:
        messagebox.showerror("Error", f"Failed to open the file: {str(e)}")
