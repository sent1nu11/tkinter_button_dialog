import tkinter as tk
from tkinter import filedialog as fd


def callback():
    name = fd.askopenfilename()
    print(name)


errmsg = 'Error!'
filename = tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)
print(f"filename : {filename}")
tk.mainloop()