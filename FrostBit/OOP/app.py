import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

#inherit from tk
#Make it a copy of tk
class HelloWorld(tk.Tk):
	def __init__(self):
		#call the constructor of tk
		super().__init__()

		self.title("Hello World!")

		ttk.Label(self, text="Hello, World!").pack()

root = HelloWorld()
root.mainloop()