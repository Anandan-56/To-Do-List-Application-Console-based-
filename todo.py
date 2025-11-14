# todo.py
# Task 2: Console-based To-Do List Application
# Implements a simple to-do manager using lists and file handling.

FILENAME = "tasks.txt"

def read_tasks():
    """Load tasks from text file into a list."""
    tasks = []
    try:
        file = open(FILENAME, "r")
        for task in file:
            task = task.strip()
            if task:
                tasks.append(task)
        file.close()
    except FileNotFoundError:
        pass
    return tasks

def write_tasks(tasks):
    """Write all tasks back to the text file."""
    file = open(FILENAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def display_tasks(tasks):
    """Show all current tasks."""
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return
    
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print()

def add_new_task(tasks):
    """Add a task entered by the user."""
    task = input("Enter task to add: ").strip()
    if task:
        tasks.append(task)
        write_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Empty task cannot be added.")

def delete_task(tasks):
    """Remove a task based on user-selected number."""
    display_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter the task number to remove: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    number = int(choice)

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        write_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print("Task number out of range.")

def main():
    tasks = read_tasks()

    while True:
        print("""
====== To-Do List ======
1. Show tasks
2. Add task
3. Remove task
4. Exit
""")

        option = input("Select an option (1-4): ")

        if option == "1":
            display_tasks(tasks)
        elif option == "2":
            add_new_task(tasks)
        elif option == "3":
            delete_task(tasks)
        elif option == "4":
            print("Exiting program. Your tasks are saved.")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
