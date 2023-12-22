
#* Modules
import customtkinter 
import tkinter as tk
from CTkMenuBar import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#? Temporary placement
def open_file():
    print("File opened!")
    
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercury")
        self.root.geometry("600x400")
        
        #* GUI components
        self.menu_bar()
    
    def menu_bar(self):
        button = customtkinter.CTkButton(self.root, text="CTkButton")

        dropdown = CustomDropdownMenu(widget=button)
        dropdown.add_option(option="value") 
        dropdown.add_separator() 

        menu = CTkMenuBar(master=self.root)
        m1 = menu.add_cascade("File")

        file_dropdown = CustomDropdownMenu(widget=m1)
        file_dropdown.add_option(option="New File")
        file_dropdown.add_option(option="Open", command=open_file)
        file_dropdown.add_option(option="Save")
        file_dropdown.add_option(option="Save As")
        file_dropdown.add_separator()
        file_dropdown.add_option(option="Quit")

        menu.add_cascade("Edit")
        menu.add_cascade("Settings")
        menu.add_cascade("About")
    
    def run(self):
        # Start the main event loop
        self.root.mainloop()

#* widgets
#! Commands removed for now 
#! These include open_file, theme_selection, help_us

# menu_bar = tkinter.Menu(root, background='blue', fg='black')
# m1 = tkinter.Menu(menu_bar, tearoff=0)
# m1.add_command(label="Open File")
# m1.add_separator()
# m1.add_command(label="Save File")
# root.config(menu=menu_bar)

# menu_bar.add_cascade(label="File",menu=m1)
# m2 = tkinter.Menu(menu_bar, tearoff=0)
# m2.add_command(label="Light theme")
# m2.add_command(label="Dark theme")
# m2.add_separator()
# m2.add_command(label="System theme")
# root.config(menu=menu_bar)
# menu_bar.add_cascade(label="Setting",menu=m2)

# m3 = tkinter.Menu(menu_bar, tearoff=0)
# m3.add_command(label="help!")

# root.config(menu=menu_bar)
# menu_bar.add_cascade(label="Help",menu=m3)

# textbox = customtkinter.CTkTextbox()


