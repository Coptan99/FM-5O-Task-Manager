import os
import shutil
import tkinter as tk
from tkinter import messagebox, simpledialog

def get_vault_paths(file_path):
    vault_paths = []
    with open(file_path, "r") as f:
        for line in f:
            if line.startswith("Vault path:"):
                vault_paths.append(line.strip().split(": ")[1])
    return vault_paths

def choose_vault_from_list(vault_paths, vault_names):
    root = tk.Tk()
    root.withdraw()
    chosen_vault_name = simpledialog.askstring("Select Vault", "Choose a vault:",
                                               parent=root,
                                               initialvalue=vault_names[0])
    if chosen_vault_name is None:
        return None

    chosen_vault_index = vault_names.index(chosen_vault_name)
    chosen_vault_path = vault_paths[chosen_vault_index]
    return chosen_vault_path

# Path to the "vaults.txt" file
file_path = "vaults.txt"
old_paths_file_path = "Paths.txt"

# Get the vault paths from the file
vault_paths = get_vault_paths(file_path)

# Strip the last folder name from each vault path
vault_names = [os.path.basename(path) for path in vault_paths]

# Choose a vault from the list
chosen_vault = choose_vault_from_list(vault_paths, vault_names)

# Display the chosen vault
if chosen_vault:
    messagebox.showinfo("Chosen Vault", f"You chose: {chosen_vault}")
    old_file_path = "old_file_path.txt"  # Replace with the actual file path to be moved

    # Move the file to the chosen vault
    new_file_path = os.path.join(chosen_vault, os.path.basename(old_file_path))
    shutil.move(old_file_path, new_file_path)

    # Remove the old path from the old Paths.txt file
    with open(old_paths_file_path, "r") as old_paths_file:
        old_paths = old_paths_file.readlines()

    old_paths = [path.strip() for path in old_paths if path.strip() != old_file_path]

    with open(old_paths_file_path, "w") as old_paths_file:
        old_paths_file.write("\n".join(old_paths))

    # Add the new path to the new vault's Paths.txt file
    new_vault_paths_file = os.path.join(chosen_vault, "Paths.txt")
    with open(new_vault_paths_file, "a") as new_paths_file:
        new_paths_file.write(f"{new_file_path}\n")
