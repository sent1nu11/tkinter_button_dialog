from tkinter import *
from tkinter import filedialog
import os

class GUI:
    def __init__(self):
        self.root = Tk()
        self.filename = ""

        #root.filename = filedialog.askopenfilename(initialdir="/C")
        theLabel = Label(self.root, text="The Editor")
        theLabel.grid(row=0)

        button1 = Button(self.root, text="Browse", command=self.open)
        button2 = Button(self.root, text="Run", command=self.other_func)
        button3 = Button(self.root, text="Quit", command=self.root.quit)

        button1.grid(row=1)
        button2.grid(row=2)
        button3.grid(row=3)

        self.root.mainloop()

    def open(self):
        result = filedialog.askopenfilename(initialdir="C:/")
        print("Function open read:")
        print(result)
        return result

    def other_func(self):
        print(result)

display = GUI()
file_path = display.open()
print(f'file_path: {file_path}')
