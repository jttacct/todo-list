import json
from datetime import datetime
# Modify todo_list to store tasks with a "completed" status
todo_list = []

# Load tasks from file
def load_tasks():
    global todo_list
    try:
        with open("tasks.json", "r") as file:
            todo_list = json.load(file)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")
    except json.JSONDecodeError:
        print("File found, but it seems to be corrupted. Starting fresh.")

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(todo_list, file)
    print("Tasks saved successfully!")

    


def add_task():
    task = input("Enter a task: ")
    category = input("Enter category (e.g., Work, Personal): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Using today's date.")
        due_date = datetime.now().date()
    
    todo_list.append({"task": task, "completed": False, "category": category, "due_date": str(due_date)})
    print(f"Task '{task}' added under '{category}' category with due date {due_date}!")
    


def view_tasks():
    if len(todo_list) == 0:
        print("No tasks yet!")
    else:
        print("\nTasks:")
        for index, item in enumerate(todo_list):
            status = "[X]" if item["completed"] else "[ ]"
            print(f"{index + 1}. {status} {item['task']} - {item['category']} - Due: {item['due_date']}")
    print()



def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["completed"] = True
            print(f"Task '{todo_list[task_num]['task']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Run the menu
menu()

