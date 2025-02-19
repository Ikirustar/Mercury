import customtkinter as ctk
import os
import sys
import terminal as trm
from tkinter import filedialog
from datetime import datetime


class JournalApp(ctk.CTk):
    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        #### ! Variables ####
        self.journal_path = None
        self.journal_entry = None
        self.edit_window = None

        self.geometry(f"{700}x{500}")
        self.title("Journal App")
        self.grid_columnconfigure((0, 1), weight=0)
        self.grid_columnconfigure((2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # * side frame

        # frame creation
        self.side_frame = ctk.CTkFrame(self, corner_radius=5)
        self.side_frame.grid(column=0, row=0, columnspan=2,
                             rowspan=6, pady=10, padx=10, sticky="nsew")

        # side frame buttons
        self.create_button = ctk.CTkButton(
            self.side_frame, text="Open", fg_color="dodger blue", height=35, corner_radius=20, command=self.open_explorer_event)
        self.create_button.grid(column=0, row=0, pady=10, padx=10)
        self.open_button = ctk.CTkButton(
            self.side_frame, text="Create", fg_color="dodger blue", height=35, corner_radius=20, command=self.create_journal)
        self.open_button.grid(column=0, row=1, pady=10, padx=10)

        # Add a spacer row with weight to push the buttons to the bottom
        self.side_frame.grid_rowconfigure((2, 3), weight=1)

        self.terminal_button = ctk.CTkButton(
            self.side_frame, text="Terminal", fg_color="black", text_color="white", height=35, corner_radius=20, command=trm.terminal_mode)
        self.terminal_button.grid(
            column=0, row=4, pady=10, padx=10, sticky="s")
        self.quit_button = ctk.CTkButton(
            self.side_frame, text="Quit", fg_color="red4", height=35, corner_radius=20, command=exit)
        self.quit_button.grid(column=0, row=5, pady=10, padx=10, sticky="s")

        # * main frame

        # frame creation
        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=5)
        self.main_frame.grid(column=2, row=1, columnspan=3,
                             rowspan=4, pady=10, padx=20, sticky="nsew")
        self.journal_entry = ctk.CTkLabel(
            self.main_frame, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.journal_entry.grid(
            column=0, row=0, pady=10, padx=10, sticky="nsew")

        # * main buttons
        self.edit_button = ctk.CTkButton(
            self, text="Edit", fg_color="dodger blue", height=40, width=40, corner_radius=15, command=self.open_edit_window)
        self.edit_button.grid(column=4, row=5, sticky="e",
                              pady=10, padx=(10, 20))

    def open_explorer_event(self):
        print("Opening file explorer\n")
        self.journal_path = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Select a file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if self.journal_path:
            with open(self.journal_path, "r") as file:
                content = file.read()

            self.journal_entry.configure(text=content)

    def create_journal(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.journal_path = filedialog.asksaveasfilename(
            initialdir=os.getcwd(), title="Create Journal", initialfile=f"{current_date}.txt", defaultextension=".txt", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if self.journal_path:
            with open(self.journal_path, "w") as file:
                file.write("")
                self.journal_entry.configure(text="")

    def open_edit_window(self):
        print("Opening edit window\n")
        if self.edit_window is None or not self.edit_window.winfo_exists():
            current_content = self.journal_entry.cget("text")
            self.edit_window = EditWindow(
                self, content=current_content, path=self.journal_path)
            self.edit_window.after(10, self.edit_window.lift)
        else:
            self.edit_window.focus()


class EditWindow(ctk.CTkToplevel):
    def __init__(self, master, content="", path=None, *args, fg_color=None, **kwargs):
        super().__init__(master, *args, fg_color=fg_color, **kwargs)
        self.geometry(f"{600}x{500}")
        self.title("Edit Journal Entry")
        self.journal_path = path

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # * journal entry textbox

        # textbox creation
        self.textbox = ctk.CTkTextbox(self, wrap="word", font=(
            "Arial", 14), corner_radius=5)
        self.textbox.grid(column=0, row=0, columnspan=7, rowspan=4,
                          padx=20, pady=20, sticky="nsew")
        self.textbox.insert("1.0", content)

        # * Edit buttons and sliders

        # font size slider
        self.font_size_slider = ctk.CTkSlider(
            self, width=200, from_=1, to=30, command=self.change_font_size)
        self.font_size_slider.set(14)  # Set initial font size
        self.font_size_slider.grid(column=0, row=5, columnspan=5,
                                   padx=20, pady=10, sticky="w")

        self.font_style_optlist = ctk.CTkOptionMenu(self, width=100, values=[
                                                    "Arial", "Times New Roman", "Courier New"], command=self.change_font_style)
        self.font_style_optlist.grid(
            column=4, row=5, padx=10, pady=10, sticky="e")

        # word count label
        self.wordcount_label = ctk.CTkLabel(
            self, text=" Max Word Count", font=("Arial", 14))
        self.wordcount_label.grid(column=0, row=4, padx=(40, 10), pady=10)

        # word count bar
        self.max_wordcount_bar = ctk.CTkProgressBar(
            self, width=400, height=15, corner_radius=10)
        self.max_wordcount_bar.grid(
            column=4, columnspan=4, row=4, padx=10, pady=10)

        # * Close and Save buttons

        # close button
        self.close_button = ctk.CTkButton(
            self, text="Close", fg_color="red4", height=40, width=40, corner_radius=15, command=self.save_entry)
        self.close_button.grid(column=5, row=5, sticky="we", padx=10)

        # save button
        self.save_button = ctk.CTkButton(
            self, text="Save", fg_color="dodger blue", height=40, width=40, corner_radius=15, command=self.save_entry)
        self.save_button.grid(column=6, row=5, sticky="we",
                              padx=10)

    def change_font_size(self, value):
        new_font = (self.textbox.cget("font")[0], int(value))
        self.textbox.configure(font=new_font)

    def change_font_style(self, value):
        new_font = (value, self.textbox.cget("font")[1])
        self.textbox.configure(font=new_font)

    def save_entry(self):
        content = self.textbox.get("1.0", "end-1c")
        self.master.journal_entry.configure(text=content)
        if self.journal_path:
            with open(self.journal_path, "w") as file:
                file.write(content)
        self.destroy()


def main():
    app = JournalApp()
    app.mainloop()


if __name__ == "__main__":
    main()
