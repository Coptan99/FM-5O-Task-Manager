import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog

# Take destination path as input



def move_vault(source_path, destination_path):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_path):
            raise FileNotFoundError("Source directory does not exist")

        # Check if the destination directory already exists
        if os.path.exists(destination_path):
            raise FileExistsError("Destination directory already exists")

        # Move the vault directory
        shutil.move(source_path, destination_path)
        print("Vault directory moved successfully")

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

# Open the file dialog to select the destination directory
destination_path = filedialog.askdirectory(title="Select the destination directory for the vault")

# Check if a directory was selected
if not destination_path:
    print("No destination directory selected")
    sys.exit(1)

# Call the move_vault function
move_vault(source_path, destination_path)
