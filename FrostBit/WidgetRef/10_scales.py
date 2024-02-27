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

#Define the handle function
def handle_scale_change(event):
	print(scale.get())

current_value = tk.DoubleVar()

#Define the scale
scale = ttk.Scale(
	root,
	orient="horizontal",
	from_=0,
	to=10,
	command=handle_scale_change,
	variable=current_value)
scale.pack(fill="x")

#scale["state"] = "disabled" # "normal"

root.mainloop()



