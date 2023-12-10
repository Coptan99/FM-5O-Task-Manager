import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog

def rename_vault(source_path, new_name):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_path):
            raise FileNotFoundError("Source directory does not exist")

        # Get the parent directory of the source directory
        parent_dir = os.path.dirname(source_path)

        # Create the new path with the renamed directory
        new_path = os.path.join(parent_dir, new_name)

        # Check if the new path already exists
        if os.path.exists(new_path):
            raise FileExistsError("New name already exists")

        # Rename the vault directory
        shutil.move(source_path, new_path)
        print("Vault directory renamed successfully")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except FileExistsError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file dialog to select the source directory
source_path = filedialog.askdirectory(title="Select the source directory for the vault")

# Check if a directory was selected
if not source_path:
    print("No source directory selected")
    sys.exit(1)

# Prompt the user to enter the new name for the vault directory
new_name = input("Enter the new name for the vault directory: ")

# Call the rename_vault function
rename_vault(source_path, new_name)
