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

#set the initial value to be displayed
initial_value = tk.StringVar(value=20)
#set the parameters of the spinbox
spin_box = ttk.Spinbox(
	root,
	from_=0,
	to=30,
	#instead of from to, you can pass in a set of values to be cycled through as well
	#values = (5, 10, 15, 20, 25, 30)
	textvariable=initial_value,
	#wrap determines if the value pacmans from top value back around to zero or vice versa
	wrap=False
)
spin_box.pack()

print(spin_box.get())

root.mainloop()



