import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog

def create_vault(vault_path):
    try:
        # Check if the vault directory already exists
        if os.path.exists(vault_path):
            raise FileExistsError("Vault directory already exists")

        # Create the vault directory
        os.makedirs(vault_path)
        print("Vault directory created successfully")

    except FileExistsError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Clean up the partially created vault directory if any error occurs
        if os.path.exists(vault_path):
            shutil.rmtree(vault_path)
        sys.exit(1)

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file dialog to select a directory
vault_path = filedialog.askdirectory(title="Select a directory for the vault")

# Check if a directory was selected
if vault_path:
    # Call the create_vault function
    create_vault(vault_path)
else:
    print("No directory selected")

# Store the vault path in a text file
# check if the file already exists
if os.path.exists("Vaults.txt"):
    with open("Vaults.txt", "a") as f:
        f.write(f"\nVault path: {vault_path}")
else:
    with open("Vaults.txt", "w") as f:
        f.write(f"Vault path: {vault_path}")
