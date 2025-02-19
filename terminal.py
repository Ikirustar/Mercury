# Program Name: Murcury
# Purpose: testing my capabilities of creating a functioning customtkinter program
# Developer: Roderick Azevedo
# Date: 8/10/2024

import os
import sys
from datetime import datetime


class term_col:
    BLACK = '\033[30m'
    RED = '\033[31m'
    DARK_RED = "\033[38;5;88m"
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'


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

    entryFile.close()

    # print results
    print(term_col.GREEN +
          f"\nJournal entry saved to {entryFileName}" + term_col.RESET)


def open_journal():
    try:
        os.chdir("Journal Entries")

        # Display directory
        files = os.listdir('.')
        list_journals = []
        list_num = 0

        print("")
        for journal in files:
            list_num += 1
            list_journals.append(journal)
            print(str(list_num) + ". " + journal)

        choice = input('\nSelect a journal: ')
        print("")

        # Display journal
        journal_choice = list_journals[int(choice) - 1]
        with open(journal_choice, "r") as entryFile:
            print(entryFile.read())

        entryFile.close()

        # Switch back to previous directory
        os.chdir("..")
    except OSError as e:
        print("\nJournal entries not found\n")
        print(term_col.DARK_RED + str(e) + term_col.RESET)


def terminal_mode():
    # * Menu
    while True:
        print("")
        print("1. Journal")
        print("2. Quit")
        print("")
        choice = input('Select an option: ')

        # ! Temporary path
        os.chdir(os.getcwd())

        if choice == "1":
            # * Journaling
            print("")
            print("1. Create")
            print("2. Open")
            print("")
            choice = input('Select an option: ')

            if choice == "1":
                create_journal()
            elif choice == "2":
                open_journal()
                exit_input = input("\nPress any button to exit: ")
        elif choice == "2":
            # * Exit
            sys.exit()
        else:
            print("\nInvalid option. Please select a valid option.\n")


def main():
    terminal_mode()


if __name__ == "__main__":
    main()
