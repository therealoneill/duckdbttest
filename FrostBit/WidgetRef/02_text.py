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

#Simple text, you create 8 lines of input and can retrieve them as required
text = tk.Text(root, height=8)
text.pack()
#Set the position you want the cursor to start entering text
#1.0 is first line(1) and zero charcter
text.insert("1.0", "Please enter some text....")
#You can disable a text box using it's state
#text["state"] = "disabled"
text["state"] = "normal" # you can write when normal

#get the text content from the widget - note this will only get was has been applied previously
#get from poistion 1 and take to the end
text_content = text.get("1.0", "end")
#This runs when the widget runs - really need buttons and functions to use properly
print(text_content)


root.mainloop()



