import tkinter as tk
from tkinter import ttk

def greet():
	#or returns the second value if the first doesn't can fed in
	print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()

#Create a variable for the textvariable below
user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
#Note calling the variable above
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
#Focus will focus the cursor on opening
name_entry.focus()


#A button calling the outside function of 'greet'
greet_button = ttk.Button(root, text="Greet", command=greet)
#Remember to pack!
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
#pack to the side left
#fill will make the button fill the widget
#Expnd will make it take up all the space
quit_button.pack(side="right")

#All python code will pause until this is closed
root.mainloop()





