-- Purpose -- 

Inputing data from obsidian and using ai to pull the best ideas at the right circumstance. This will sync with a user's notes and calender, and bring up different reminders or different ideologies based on the events. The goal is to Helps user's implant the best "thought generaters" to produce good "thought bubbles". If people get exposed to something for more than 4 months, it typically becomes a part of them. It will be a good planning tool for task management, predictive modeling/machine learning, and a good place to store information/knowledge. Machine learning algorithims will also adapt to the users, and automation features will become more readily available. The goal is to speed up the efficiency of how information flows, and develop a fast way to learn information and bring it back up. 

-- Features --

**Questionable or doesn't make sense**

- Built in note taking functionality.
- Import obsidian vaults/onenote/txt/md files. 
	- This will be basis for what ideas the AI pulls. Random ideas or ideologies that may have been forgotten about, could be useful on a certain day.
	- Reminders could also be stored, and they could be brought up again.
	- Information such as current Activities and responsibilities could be brought up again
     		(If a user somehow forgets what they are currently enrolled in or something like that)
   	  		- The data should ideally be in a large scale format. **Possibly a database structure or even as far as a sql server**.
- AI integegration using langchain and API key. GPT4 will be used for now
	-  google gemini on the lookout.
- Basic data analysis functionality. Putting in data and using matplotlib to display data. 
	- Data agregation and cleaning tools also provided
	- Regression modeling, Linear interpolation, ect
- Planning/Project management functionality.
	- Similar to productivity tools like clickup, monday, and trello. Features ghant charts, timeline, calenders, ect. 
- Premade ai prompts for common usage, such as ability to put in tasks as parameters, and having gpt4 automatically planning out the day based on 
	priority. <-- using a ai prompt specifically designed for this functionality.
- Automation for various miniscule tasks.
	- Machine learning algorithims can adapt to a user's note taking style, and take personal notes from whatever resource desireable.
 	- Looking through notes and noticing gaps of information.
  		- Possibly combining the best ideas/idelogies from different sources. 

** Languages **
- Current
	- Python
 	- SQL 
 	- Markdown 
- Considering
	- C#
 	- Visual Basic (Unlikely, pretty slow)
  	- C++ (If we need to maximize memory usage)
  	- Java

-- Libraries --
	- Langchain with an API Key to use GPT 4 (Looking into google gemini, as that outperforms GPT4 except for **basic logic??**)
	- Custom Tkinter 
		- GUI library to help display the program
	- Matplotlib 
		- Displaying dataframes through graphing.
  	- Numpy
  	- Sub Process
   	- Markdown

-- Custom tkinter --
	- If multiple columns have the the same attributes except for the index, they can be put together using (0, 1, 2, ect).
	- Weight influences how big the row/column is compared to the rest.
	- Grid rowspan/columnspan, can make the widget span across multiple rows/columns.
	- padx/pady is the outside space, ipadx/ipady is the space within the widget


