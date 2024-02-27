import tkinter as tk
from tkinter import ttk

# Function to quit the application
def quit_app():
    root.quit()

# Initialize the main application window
root = tk.Tk()
root.title("Full-Screen Tkinter WebApp Example")

# Make the window full-screen
root.attributes('-fullscreen', True)

# Create a frame for the widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Example of a Label
label = ttk.Label(frame, text="This is a label")
label.pack()

# Example of a Button
button = ttk.Button(frame, text="Quit", command=quit_app)
button.pack()

# Example of an Entry (text input)
entry = ttk.Entry(frame)
entry.pack()

# Example of a Text (multiline text input)
text = tk.Text(frame, height=5, width=30)
text.pack()

# Example of a Checkbox
checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(frame, text="Check me", variable=checkbox_var)
checkbox.pack()

# Example of Radio Buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(frame, text="Option 1", variable=radio_var, value="1")
radio1.pack()
radio2 = ttk.Radiobutton(frame, text="Option 2", variable=radio_var, value="2")
radio2.pack()

# Example of a Dropdown Menu (Combobox)
combo_var = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=combo_var, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

# Example of a Listbox
listbox = tk.Listbox(frame)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack()

# Run the application
root.mainloop()
