import tkinter as tk
import tkinter.font as font
from tkinter import ttk

from numpy import pad
#from windows import set_dpi_awareness

#set_dpi_awareness()
#Adding in logic for high DPI widgets
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
	pass

root = tk.Tk()
root.title("Distance Converter")

#can be set to variable later for changing
#Does not apply to all widgets - such as entry box - note the manual entry for this
font.nametofont("TkDefaultFont").configure(size=15)

#Variables for entry field
metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")
#Function to calculate feet
#adding args to prevent crash
#Valueerror is for no value case - stops crashing

def calculate_feet(*args):
	try:
		#pass
		metres = float(metres_value.get())
		feet = metres * 3.28084
		#print(f"{metres} metres is equal to {feet:.3f} feet.")
		feet_value.set(f"{feet:.3f}")
	except ValueError:
		pass


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30,15))
main.grid()

metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

#Place all widgets in the grid
metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

#Binds the return key to the keyboard for executing the only command on the app
#Look at the notes for more info on key bindings
root.bind("<Return>", calculate_feet)

root.mainloop()
