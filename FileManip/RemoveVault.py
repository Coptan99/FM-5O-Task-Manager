import os
from ChooseVault import get_vault_paths, choose_vault_from_list
from tkinter import messagebox


def remove_vault(vault_path):
    try:
        os.remove(vault_path)
        messagebox.showinfo("Vault Removed", "Vault has been successfully removed.")
    except FileNotFoundError:
        messagebox.showerror("Vault Not Found", "The specified vault file does not exist.")
    except PermissionError:
        messagebox.showerror("Permission Denied", "You don't have permission to delete the vault file.")

# Path to the "vaults.txt" file
file_path = "vaults.txt"

# Get the vault paths from the file
vault_paths = get_vault_paths(file_path)

# Strip the last folder name from each vault path
vault_names = [os.path.basename(path) for path in vault_paths]

# Choose a vault from the list
chosen_vault = choose_vault_from_list(vault_paths, vault_names)

# Remove the chosen vault
if chosen_vault:
    remove_vault(chosen_vault)
