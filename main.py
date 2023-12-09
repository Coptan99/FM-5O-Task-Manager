import tkinter as tk
from tkinter import ttk

# Initializing the gui window
app = tk.Tk()
app.title = "FM^5O"
app.configure()

entry = ttk.Entry()

main_label = ttk.Label(text="FM^5O", font=("Source Code Pro", 20), padding=10)
main_label.pack()

entry.pack()

main_button = ttk.Button(text="Submit")
main_button.pack()

# Main loop
app.mainloop()
