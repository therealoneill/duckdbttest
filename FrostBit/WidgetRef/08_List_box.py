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

#Set the list of values
programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")
#Initalize the string variable
langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended") # extended allows multiselect or "browse" for single
#note that any property in the line above can be broken out and detailed here like this for easier reading and setting
#langs_select["selectmode"] = "extended"
langs_select.pack()


#Defining the function to be used
def handle_selection_change(event):
	selected_indices = langs_select.curselection()
	#get indices of the selection - not the value
	for i in selected_indices:
		print(langs_select.get(i))

#Bind a function to an event from the list box
langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()



