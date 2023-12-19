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

# Path to the "files.txt" file
file_path = "files.txt"
old_paths_file_path = "Paths.txt"

# Get the file paths from the file
file_paths = get_file_paths(file_path)

# Choose a file from the list
chosen_file = choose_file_from_list(file_paths)

# Display the chosen file
if chosen_file:
    messagebox.showinfo("Chosen File", f"You chose: {chosen_file}")

    # Remove the file
    os.remove(chosen_file)

    # Remove the file path from the Paths.txt file
    with open(old_paths_file_path, "r") as old_paths_file:
        old_paths = old_paths_file.readlines()

    old_paths = [path.strip() for path in old_paths if path.strip() != chosen_file]

    with open(old_paths_file_path, "w") as old_paths_file:
        old_paths_file.write("\n".join(old_paths))
