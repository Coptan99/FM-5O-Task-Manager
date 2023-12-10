# Native imports
import tkinter as tk
from tkinter import ttk

# Custom imports
from functions import *

# Initializing the gui window
app = tk.Tk()
app.title("FMO")
# app.config(bg="#222222")

# Creating the widgets
entry = ttk.Entry()

# main_label = ttk.Label(text="FMO Task Manager", font=(
#     "Source Code Pro", 20), padding=10, background="#222222", foreground="#ffffff")
main_label = ttk.Label(text="FMO Task Manager", font=("Source Code Pro", 20), padding=10)
main_label.pack()

# label = ttk.Label(text="Enter your task: ", font=(
#     "Source Code Pro", 10), padding=10, background="#222222", foreground="#ffffff")
label = ttk.Label(text="Enter your task: ", font=("Source Code Pro", 10), padding=10)
label.pack()

entry.pack()

main_button = ttk.Button(text="Add", command=add_task)
main_button.pack()

# Main loop
app.mainloop()
