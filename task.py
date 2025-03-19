import json
import sys
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Adds a new task."""
    tasks = load_tasks()
    new_id = 1
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, description):
    """Updates an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    """Deletes an existing task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

def mark_task_status(task_id, status):
    """Marks a task as in progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if status in ["in-progress", "done", "todo"]:
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task {task_id} marked as {status}")
                return
            else:
                print(f"Invalid status: {status}. Must be 'todo', 'in-progress', or 'done'.")
                return
    print(f"Task {task_id} not found")

def list_tasks(status=None):
    """Lists tasks, optionally filtered by status, in a table format with borders."""
    tasks = load_tasks()
    if status:
        valid_statuses = ["done", "todo", "in-progress"]
        if status not in valid_statuses:
            print(f"Invalid status: {status}. Must be 'todo', 'in-progress', or 'done'.")
            return
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks
    if not filtered_tasks:
        print("No tasks found.")
        return

    header = ["ID", "Description", "Status", "Created", "Updated"]
    col_widths = [5, 30, 15, 25, 25]

    def print_row(row):
        print("|", end="")
        for i, col in enumerate(row):
            print(f" {col:<{col_widths[i]}} |", end="")
        print()

    def print_separator():
        print("+", end="")
        for width in col_widths:
            print("-" * (width + 2), end="+")
        print()

    print_separator()
    print_row(header)
    print_separator()
    for task in filtered_tasks:
        row = [
            task['id'],
            task['description'],
            task['status'],
            task['createdAt'],
            task['updatedAt']
        ]
        print_row(row)
        print_separator()

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task.py add <description>")
            return
        description = sys.argv[2]
        add_task(description)
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task.py update <id> <description>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        description = sys.argv[3]
        update_task(task_id, description)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        delete_task(task_id)
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task.py mark-in-progress <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        mark_task_status(task_id, "in-progress")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task.py mark-done <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be an integer.")
            return
        mark_task_status(task_id, "done")
    elif command == "list":
        if len(sys.argv) > 2:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
