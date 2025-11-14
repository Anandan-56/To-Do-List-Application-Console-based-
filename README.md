# To-Do List Manager

This project is a simple console-based To-Do List Manager developed using Python.  
It is created as part of Task 2 to demonstrate the use of lists, basic file handling with `open()`, and a menu-driven interface in the terminal.  
The application allows users to maintain a persistent list of tasks by storing them in a text file.

## Features
- Add a new task  
- View all existing tasks  
- Remove a task by its number  
- Persistent storage using a text file (`tasks.txt`)  
- Uses a Python list to manage tasks during program execution

## Tools Used
- Python  
- VS Code / Terminal  

## How the Application Works
1. Tasks are loaded from `tasks.txt` when the program starts.  
2. A menu is displayed to the user with options to:
1 - Show tasks
2 - Add task
3 - Remove task
4 - Exit

3. The selected action is performed on the list of tasks.  
4. Updated tasks are saved back to the text file using `open()` so that the data remains available for the next run.

## How to Run
1. Open the project folder in VS Code or any terminal.
2. Run the program using the command:
        ```bash
python todo.py
Sample Output
====== To-Do List ======
1. Show tasks
2. Add task
3. Remove task
4. Exit
Select an option: 2
Enter task to add: Submit assignment
Task added successfully.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8f734b75-40a7-48d6-8c3b-ed61b4660917" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d4879028-6211-431c-83a5-9480bec9b565" />

