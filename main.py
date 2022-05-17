import tkinter as tk
from tkinter import Tk, Button, filedialog, Label, ttk
import os

root = tk.Tk()
root.title("First GUI")
root.minsize(width=500, height=300)

def getFile():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                               filetypes=(("Excel file", "*.xlsx"), ("all files", "*.*")))



class myButton:
    def __init__(self):
        self.button = Button(text="press", command=getFile)
        self.button.pack()

my_button = myButton()


root.mainloop()





root.mainloop()