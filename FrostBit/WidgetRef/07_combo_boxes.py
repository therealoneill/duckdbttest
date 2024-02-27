from calendar import week
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


#Selected variable is what is used to pass events out and in
selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
#Add the following to stop people entering their own values
weekday["state"] = "readonly" # "noraml" is the counterpart that allows manual input
weekday.pack()


#Handle driver

def handle_selection(event):
	print("Today is", selected_weekday.get())
	print("But we're going to change it to Friday. ")
	selected_weekday.set("Friday")
	print(weekday.current())


#Assign to combobox
weekday.bind("<<ComboboxSelected>>", handle_selection)


root.mainloop()

print(selected_weekday.get(), " was selected.")



