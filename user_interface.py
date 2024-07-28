# Main loop, through the data
import tkinter as tk
from tkinter import messagebox

def create_ui(): 
    root = tk.Tk()
    root.title("Formular ausfüllen")
    root.geometry("300x200")

    label = tk.Label(root, text="Clicke hier um das nächste Formular zu füllen")
    label.pack(pady=20)

    button = tk.Button(root, text="Füllen", command=daten_laden)