# Program Name: Murcury Terminal
# Purpose: Creating journals and handeling tasks
# Developer: Roderick Azevedo
# Date: 9/15/2023

import os
from datetime import datetime

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
print(f"Journal entry saved to {entryFileName}")
