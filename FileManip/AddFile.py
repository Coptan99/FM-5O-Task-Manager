import tkinter as tk
from tkinter import filedialog
import os

def add_file_to_vault():
    try:
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename()

        # Check if a file was selected
        if file_path:
            # Create the vault folder if it doesn't exist
            vault_folder = "vault"
            if not os.path.exists(vault_folder):
                os.makedirs(vault_folder)

            # Get the file name from the file path
            file_name = os.path.basename(file_path)

            # Move the file to the vault folder
            new_file_path = os.path.join(vault_folder, file_name)
            os.rename(file_path, new_file_path)

            # Save the path of the file in Paths.txt
            with open("Paths.txt", "a") as f:
                f.write(new_file_path + "\n")

            print("File added to vault successfully!")
            window.destroy()  # Close the popup window
        else:
            print("No file selected.")
    except Exception as e:
        print(f"Error adding file to vault: {str(e)}")

# Create a Tkinter window (popup)
window = tk.Toplevel()
window.configure(bg="dark green")

# Create a button to add a file to the vault
add_file_button = tk.Button(window, text="Add File to Vault", command=add_file_to_vault, bg="black", fg="cyan")
add_file_button.pack()

# Start the Tkinter event loop
window.mainloop()
