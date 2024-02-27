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

check_button = ttk.Checkbutton(root, text="Clicky clicky")
check_button.pack()
#State can be defined as well
#check_button["state"] = "disabled"

#Function supported check buttons - they have many options like buttons

selected_option = tk.StringVar()

def print_current_option():
	print(selected_option.get())

check = ttk.Checkbutton(
	root,
	text="Check Example",
	variable=selected_option,
	command=print_current_option,
	onvalue="On",
	offvalue="Off"
)
check.pack()



root.mainloop()



