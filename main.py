# Program Name: Murcury Terminal
# Purpose: Creating journals and handeling tasks
# Developer: Roderick Azevedo
# Date: 9/15/2023

"""
ai prompt 

Act as my mentory and help me develop a python project. (I am familier with the syntax of Python and have expreience with a couple of libraries. 
But not an expert and I do not know frameworks and project structure). 
This project allows users to create journals and write checklists in a GUI. It is also a note taking
application that has formatting features such as different heading and intellisense. GPT4 will give suggestions on notes and be used to keep track of information any
users forget. This information is stored in a txt file. {}. 
"""

import sys
from Journal import create_journal, create_checklist


def main():
    print("gui")


def terminal():
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


if __name__ == "__main__":
    terminal()
