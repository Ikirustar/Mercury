
# * Modules
import customtkinter
import tkinter as tk
import os
from CTkMenuBar import *
from core.terminal import terminal_menu

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#! ##### Paths #####

logo_path = os.path.dirname(os.path.abspath(__file__)) + "\Images\Logo.png"

# ? Temporary placement


def open_file():
    print("File opened!")


class StartWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mercury")
        self.root.geometry("600x400")

        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # * GUI components
        self.menu_bar()
        self.start_window_widgets()

    def menu_bar(self):
        button = customtkinter.CTkButton(self.root, text="CTkButton")

        dropdown = CustomDropdownMenu(widget=button)
        dropdown.add_option(option="value")
        dropdown.add_separator()

        menu = CTkMenuBar(master=self.root)
        m1 = menu.add_cascade("File")

        file_dropdown = CustomDropdownMenu(widget=m1)
        file_dropdown.add_option(option="New File")
        file_dropdown.add_option(option="Open", command=terminal_menu)
        file_dropdown.add_option(option="Save")
        file_dropdown.add_option(option="Save As")
        file_dropdown.add_separator()
        file_dropdown.add_option(option="Quit")

        menu.add_cascade("Edit")
        menu.add_cascade("Settings")
        menu.add_cascade("About")

    #! Pack bug

    def start_window_widgets(self):
        logo_image = tk.PhotoImage(file=logo_path)
        logo_widget = tk.Label(self.root, image=logo_image)
        logo_widget.image = logo_image
        logo_widget.pack(side='top')

        # Main Frame
        main_frame = customtkinter.CTkFrame(master=self.root, width=200)
        main_frame.grid(row=3, column=3, padx=20, pady=20, sticky="nsew")

    def run(self):
        # Start the main event loop
        self.root.mainloop()
# class MainWindow:
#     def __init__(self, root):


# * widgets
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
