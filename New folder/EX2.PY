# Import the tkinter library
from tkinter import *

# Create an instance of tkinter frame
win= Tk()

# Set the size of the Tkinter window
win.geometry("700x350")

# Create an instance of MenuBar
menubar= Menu(win)
file= Menu(menubar, tearoff= 0)

# Add Menu Items
file.add_command(label= "New")
file.add_command(label= "Open")
file.add_command(label="Save")
menubar.add_cascade(label="File", menu=file)
win.config(menu=menubar)
win.mainloop()