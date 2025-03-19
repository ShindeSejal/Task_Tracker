# Task_Tracker.py
Task Tracker Build a CLI app to track your tasks and manage your to-do list
https://roadmap.sh/projects/task-tracker

****Requirements:****
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.


***OUTPUT OF THE PROGRAM****
# show a list
PS D:\program\Task Tracker> python task.py list  
![Screenshot 2025-03-20 004455](https://github.com/user-attachments/assets/a2e82d91-22f6-4426-8ef1-3ea527a612b2)

#update a list 
PS D:\program\Task Tracker> python task.py update 1 "buy groceries and cooking"
![Screenshot 2025-03-20 004542](https://github.com/user-attachments/assets/0ff9363c-8f6f-4589-88e0-6b0be197dd6a)

#delete a list 
PS D:\program\Task Tracker> python task.py delete "11"
![Screenshot 2025-03-20 004606](https://github.com/user-attachments/assets/67197c49-ae0c-4a6b-8456-e31e5585cacd)

#mark in progress list
PS D:\program\Task Tracker> python task.py mark-in-progress "1"
![Screenshot 2025-03-20 005036](https://github.com/user-attachments/assets/bef9b55e-368f-494d-a49c-8ecf9a8a0f33)

#mark done 
PS D:\program\Task Tracker> python task.py mark-done "2" 
![Screenshot 2025-03-20 005210](https://github.com/user-attachments/assets/953cb96a-6ae7-42c0-842b-6856865cde59)





