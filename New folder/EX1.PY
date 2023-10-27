# from tkinter import *

# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master

#         menu = Menu(self.master)
#         self.master.config(menu=menu)

#         fileMenu = Menu(menu)
#         fileMenu.add_command(label="New", command=self.exitProgram)
#         menu.add_cascade(label="File", menu=fileMenu)

#     def exitProgram(self):
#         exit()
        
# root = Tk()
# app = Window(root)
# root.wm_title("Tkinter window")
# root.mainloop()
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
menubar.add_cascade(label="File", menu=file)
win.config(menu=menubar)
win.mainloop()