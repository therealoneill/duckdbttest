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


#Having the same storage variable between options let them know they are grouped
storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
	root,
	text="Option 1",
	variable=storage_variable,
	value="First option"
)

option_two = ttk.Radiobutton(
	root,
	text="Option 2",
	variable=storage_variable,
	value="Second option"
)

option_three = ttk.Radiobutton(
	root,
	text="Option 3",
	variable=storage_variable,
	value="Third option"
)

#Remember to pack
option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()



