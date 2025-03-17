import json
import os
import sys

TASK_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Adds a new task."""
    tasks = load_tasks()
    new_task = {"description": description, "status": "todo"}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task: {description}")

def update_task(index, description):
    """Updates an existing task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["description"] = description
        save_tasks(tasks)
        print(f"Updated task {index}: {description}")
    else:
        print("Invalid task index.")

def delete_task(index):
    """Deletes a task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task {index}: {deleted_task['description']}")
    else:
        print("Invalid task index.")

def mark_task(index, status):
    """Marks a task as in progress or done."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        if status in ["done", "in_progress", "todo"]:
            tasks[index]["status"] = status
            save_tasks(tasks)
            print(f"Marked task {index} as {status}")
        else:
            print("Invalid status. Use 'done', 'in_progress', or 'todo'.")
    else:
        print("Invalid task index.")

def list_tasks(filter_status=None):
    """Lists tasks, optionally filtered by status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks):
        if filter_status is None or task["status"] == filter_status:
            print(f"{index}. [{task['status']}] {task['description']}")

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  add <description>")
        print("  update <index> <description>")
        print("  delete <index>")
        print("  mark <index> <done|in_progress|todo>")
        print("  list")
        print("  list done")
        print("  list in_progress")
        print("  list todo")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: add <description>")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: update <index> <description>")
            return
        try:
            index = int(sys.argv[2])
            description = " ".join(sys.argv[3:])
            update_task(index, description)
        except ValueError:
            print("Invalid index. Must be an integer.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: delete <index>")
            return
        try:
            index = int(sys.argv[2])
            delete_task(index)
        except ValueError:
            print("Invalid index. Must be an integer.")

    elif command == "mark":
        if len(sys.argv) < 4:
            print("Usage: mark <index> <done|in_progress|todo>")
            return
        try:
            index = int(sys.argv[2])
            status = sys.argv[3]
            mark_task(index, status)
        except ValueError:
            print("Invalid index. Must be an integer.")

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3:
            status = sys.argv[2]
            if status in ["done", "in_progress", "todo"]:
                list_tasks(status)
            else:
                print("Invalid status. Use 'done', 'in_progress', or 'todo'.")
        else:
            print("Usage: list [done|in_progress|todo]")

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()