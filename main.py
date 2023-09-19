# Program Name: Murcury Terminal
# Purpose: Creating journals and handeling tasks
# Developer: Roderick Azevedo
# Date: 9/15/2023

import os
import sys
from datetime import datetime


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
    # Similar to the old version. Needs to be updated

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


while True:
    # Menu
    print("1. Journal")
    print("2. Checklist")
    print("3. Quit")
    choice = input('Select an option: ')

    if choice == "1":
        create_journal()
    elif choice == "2":
        create_checklist()
    elif choice == "3":
        sys.exit()
    else:
        print("\nInvalid option. Please select a valid option.\n")
