import tkinter as tk
#Pillow or PIL is an image loading app
from PIL import Image,ImageTk
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

#plain label
label = ttk.Label(root, text="Hello Sailor!", padding=10)
label.pack(side="top")

#Font applied
label2 = ttk.Label(root, text="How ya Doing?", padding=10)
label2.config(font=("Segoe UI", 20))
label2.pack(side="top")

#Apply picture unsing PIL - pip install pillow
image = Image.open("D:\\github\\FrostBit\\WidgetRef\\angwy_Cici.jpg").resize((100,100))
photo = ImageTk.PhotoImage(image)
label3 = ttk.Label(root, image=photo, padding=5)
label3.pack()

#Apply text & picture compound unsing PIL - pip install pillow
image2 = Image.open("D:\\github\\FrostBit\\WidgetRef\\angwy_Cici.jpg").resize((100,100))
photo2 = ImageTk.PhotoImage(image2)
label4 = ttk.Label(root, text="woof woof", image=photo2, padding=5, compound="left")
label4.pack()


#dynamic label - can react to variables, scripting
dynamicLabel = tk.StringVar()

label5 = ttk.Label(root, padding=10, textvariable=dynamicLabel)
label5.pack()

dynamicLabel.set("I am dynamic")

root.mainloop()



