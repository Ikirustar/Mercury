
#* Program Name: Murcury Terminal
#* Purpose: Creating journals and handeling tasks
#* Developer: Roderick Azevedo
#* Date: 9/15/2023

#? ai prompts 

"""
Act as my mentory and help me develop a python project. (I am familier with the syntax of Python and have expreience with a couple of libraries. 
But not an expert and I do not know frameworks and project structure). 
This project allows users to create journals and write checklists in a GUI. It is also a note taking
application that has formatting features such as different headings and intellisense. GPT4 will give suggestions on notes and be used to keep track of information any
users forget. This information is stored in a txt file. {}. <--- Follow up with whatever question


Give me an explanation for how I can implement this feature {}
"""

import sys
from customtkinter import CTk
from gui.windows import StartWindow
from core.terminal import create_journal, create_checklist

if __name__ == "__main__":
    root = CTk()
    app = StartWindow(root)
    app.run()






















