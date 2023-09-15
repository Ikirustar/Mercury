# Program Name: Murcury Terminal
# Purpose: Creating journals and handeling tasks
# Developer: Roderick Azevedo
# Date: 9/15/2023

import os
from datetime import datetime

while True:
    # Menu
    print("1. Journal")
    print("2. Checklist")
    print("3. Quit")
    choice = input('Select an option: ')

    if choice == "1":
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
    else:
        print("\nInvalid option. Please select a valid option.\n")
