import tkinter as tk
from tkinter import ttk

root = tk.Tk()
#Place the element in the root (or main window) - add padding and remember to pack
ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()



#All python code will pause until this is closed
root.mainloop()





