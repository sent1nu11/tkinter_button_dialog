import tkinter as tk
from tkinter import Tk, Button, filedialog, Label, ttk
import os

root = tk.Tk()
root.title("First GUI")
root.minsize(width=500, height=300)

# def getFile():
#     filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
#                                filetypes=(("Excel file", "*.xlsx"), ("all files", "*.*")))
#     print(filename)




class GetFile:

    file_name = ''
    def __init__(self):
        self.filename = None
        self.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("Excel file", "*.xlsx"), ("all files", "*.*")))

    def filename(self, x):
        self.filename = x




class myButton:
    def __init__(self):
        self.button = Button(text="press", command= lambda: file_name.filename)
        self.button.pack()

my_button = myButton()
file_name = GetFile()
print(file_name)

root.mainloop()





root.mainloop()