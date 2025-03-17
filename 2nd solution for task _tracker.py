import json
import os
import sys

TASKS_FILE = "tasks.json"

# Ensure the file exists, if not create it
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

# Helper function to load from json file
def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Helper function to save tasks to json file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to list tasks by status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"{task['title']} - {task['status']}: {task['description']}")

# Function to add a task
def add_task(title, description):
    tasks = load_tasks()
    new_task = {
        "title": title,
        "description": description,
        "status": "not done"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added.")

# Function to delete a task
def delete_task(title):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['title'] != title]
    save_tasks(tasks)
    print(f"Task '{title}' deleted.")

# Function to update a task's status
def update_task(title, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['title'] == title:
            task['status'] = new_status
            save_tasks(tasks)
            print(f"Task '{title}' updated to '{new_status}' status.")
            return
    print(f"Task '{title}' not found.")

# Main CLI handler
def main():
    if len(sys.argv) < 2:
        print("usage: python task.py [command] [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == 'add':
        if len(sys.argv) != 4:
            print("Usage: python task.py add [title] [description]")
            sys.exit(1)
        title = sys.argv[2]
        description = sys.argv[3]
        add_task(title, description)

    elif command == 'update':
        if len(sys.argv) != 4:
            print("Usage: python task.py update [title] [status]")
            sys.exit(1)
        title = sys.argv[2]
        new_status = sys.argv[3].lower()
        if new_status not in ['not done', 'in progress', 'done']:
            print("Invalid status. Status must be 'not done', 'in progress', or 'done'.")
            sys.exit(1)
        update_task(title, new_status)

    elif command == 'delete':
        if len(sys.argv) != 3:
            print("Usage: python task.py delete [title]")
            sys.exit(1)
        title = sys.argv[2]
        delete_task(title)

    elif command == 'list':
        if len(sys.argv) == 3:
            status = sys.argv[2].lower()
            if status not in ['not done', 'in progress', 'done']:
                print("Invalid status. Status must be 'not done', 'in progress', or 'done'.")
                sys.exit(1)
            list_tasks(status)
        else:
            list_tasks()

    elif command == 'done':
        if len(sys.argv) != 3:
            print("Usage: python task.py done [title]")
            sys.exit(1)
        title = sys.argv[2]
        update_task(title, 'done')

    elif command == 'inprogress':
        if len(sys.argv) != 3:
            print("Usage: python task.py inprogress [title]")
            sys.exit(1)
        title = sys.argv[2]
        update_task(title, 'in progress')

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()


