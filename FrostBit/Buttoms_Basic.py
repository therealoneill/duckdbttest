import tkinter as tk
from tkinter import ttk

def greet():
	print("Hello, World!")

root = tk.Tk()

#A button calling the outside function of 'greet'
greet_button = ttk.Button(root, text="Greet", command=greet)
#Remember to pack!
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
#pack to the side left
#fill will make the button fill the widget
#Expnd will make it take up all the space
quit_button.pack(side="left", fill="both", expand=True)

#All python code will pause until this is closed
root.mainloop()





