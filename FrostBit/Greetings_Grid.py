import tkinter as tk
from tkinter import EW, ttk

#Adding in logic for high DPI widgets
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
	pass


def greet():
	#or returns the second value if the first doesn't can fed in
	print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()
root.title ("Stinky")

user_name = tk.StringVar()

#Need to set the column configuratoes
#weigh is relative - higher number is more imporant
root.columnconfigure(0, weight=1)


#Grid fills row by row if nothing set
#Use row or column or both to set where the widgets will appear

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

#Let's create another frame
buttons = ttk.Frame(root, padding=(20, 10))
#NOte the sticky command
buttons.grid(sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

#All python code will pause until this is closed
root.mainloop()





