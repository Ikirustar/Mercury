# Program Name: Murcury Terminal
# Purpose: Creating journals and handeling tasks
# Developer: Roderick Azevedo
# Date: 9/15/2023

import os
from datetime import datetime


def create_journal():
    # Create directory
    journaldir = "Journal Entries"
    os.makedirs(journaldir, exist_ok=True)

    # Get current date
    now = datetime.now()
    entryDate = now.strftime("%Y-%H-%M")

    # Create File
    entryFileName = f"{journaldir}/{entryDate}.txt"
    with open(entryFileName, "w") as entryFile:
        entryText = input("Enter your journal entry: ")
        entryFile.write(entryText)

    # print results
    print(f"\nJournal entry saved to {entryFileName}\n")


def create_checklist():
    # Create directory
    checklistdir = "Checklist"
    os.makedirs(checklistdir, exist_ok=True)

    # Create checklist
    checklistname = input("Enter a checklist name: ")
    checklistFileName = f"{checklistdir}/{checklistname}.txt"

    # Put checklist items in txt file
    checklistItem = input("Enter checklist item:\n")
    with open(checklistFileName, "a") as checklist:
        checklist.write(f"[]{checklistItem}\n")
    print("Checklist item added")


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
    else:
        print("\nInvalid option. Please select a valid option.\n")
