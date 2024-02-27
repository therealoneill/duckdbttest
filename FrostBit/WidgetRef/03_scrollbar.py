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

text = tk.Text(root, height=8)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Please enter a comment...")

#Adding a scrollbar
#In ttk a scrollbar and a text box are separate entities
#orient is moving the scrollbar up and down
#command - what we want the scrollbar do - move the text in a y direction
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")
#you need to link a scrollbar to the text to see the text moving
text["yscrollcommand"] = text_scroll.set


root.mainloop()



