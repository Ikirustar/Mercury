
import customtkinter
import os
import sys
from datetime import datetime


class App(customtkinter.CTk):
    WIDTH = 900
    HEIGHT = 480

    def __init__(self):
        super().__init__()

        self.title("Mercury")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsw")

        # * OS-Bot frames

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self,
            corner_radius=0,
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=50, pady=20)

        # * Buttons
        self.terminal_button = customtkinter.CTkButton(
            self, text="Terminal", corner_radius=50, height=40, fg_color="black", text_color="white", command=mercury_terminal)
        self.terminal_button.grid(
            row=0, column=0, sticky="sew", padx=20, pady=30)

        self.open_button = customtkinter.CTkButton(
            self, text="Open", corner_radius=50, height=40)
        self.open_button.grid(row=0, column=0, sticky="new", padx=20, pady=30)

        self.save = customtkinter.CTkButton(
            self, text="Save", corner_radius=50, height=40)
        self.save.grid(row=0, column=0, sticky="new", padx=20, pady=(80, 20))

        self.save_as_button = customtkinter.CTkButton(
            self, text="Save As", corner_radius=50, height=40)
        self.save_as_button.grid(
            row=0, column=0, sticky="new", padx=20, pady=(130, 20))


def create_journal():
    # Create directory
    journaldir = "Journal Entries"
    os.makedirs(journaldir, exist_ok=True)

    # Get current date
    now = datetime.now()
    entryDate = now.strftime("%Y-%m-%d")

    # Create File
    entryFileName = f"{journaldir}/{entryDate}.txt"
    with open(entryFileName, "w") as entryFile:
        entryText = input("Enter your journal entry: ")
        entryFile.write(entryText)

    # print results
    print(f"\nJournal entry saved to {entryFileName}\n")


def create_checklist():
    try:
        # Create directory
        checklistdir = "Checklist"
        os.makedirs(checklistdir, exist_ok=True)

        # Create checklist
        checklistname = input("Checklist name: ")
        checklistPath = os.path.join(checklistdir, checklistname)
        os.makedirs(checklistPath, exist_ok=True)
        os.chdir(checklistPath)
        checklistStart = True
    except:
        print("\nChecklist already exists\n")

        return

    print("\nType stop to finish")
    while checklistStart == True:
        try:
            list = input("-")
            if list.upper() == "STOP":
                print("\nSaved\n")
                os.chdir("..")
                break
            else:
                os.mkdir("-" + list)
        except:
            print("\nItem already exists\n")
    os.chdir("....")


def mercury_terminal():
    # Menu
    print("1. Journal")
    print("2. Checklist")
    print("3. Quit")
    choice = input('Select an option: ')

    # ! Temporary path
    os.chdir("C:\\Users\\platf\\OneDrive\\Desktop\\Projects\\Mercury")

    if choice == "1":
        create_journal()
    elif choice == "2":
        create_checklist()
    elif choice == "3":
        sys.exit()
    else:
        print("\nInvalid option. Please select a valid option.\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
