import tkinter as tk
from tkinter import ttk
#from windows import set_dpi_awareness

#set_dpi_awareness()
#Adding in logic for high DPI widgets
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
	pass

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Label(root, text="What ya doing boy?", padding=20).pack()

#Note the fill in x direction required for the seprtr to show - sticky works too
ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="What ya doing boy?", padding=20).pack()


root.mainloop()



