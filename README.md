# task-tracker

Task Tracker CLI

A simple Command Line Interface (CLI) application to manage and track tasks.

Features

- Add Tasks
- Update Tasks
- Delete Tasks
- Mark Tasks as In Progress
- Mark Tasks as Done
- List All Tasks
- List Tasks by Status
- Store Tasks in JSON File
- Automatic Task ID Generation

---

Project Structure

task-tracker/

├── task_cli.py

├── tasks.json

└── README.md

---

Requirements

- Python 3.x

No external libraries are required.

---

How to Run

Navigate to the project directory:

cd task-tracker

Run commands using:

python task_cli.py <command>

---

Commands

Add Task

python task_cli.py add "Buy groceries"

Output:

Task added successfully (ID: 1)

---

Update Task

python task_cli.py update 1 "Buy groceries and cook dinner"

Output:

Task updated successfully

---

Delete Task

python task_cli.py delete 1

Output:

Task deleted successfully

---

Mark Task In Progress

python task_cli.py mark-in-progress 1

Output:

Task marked as in-progress

---

Mark Task Done

python task_cli.py mark-done 1

Output:

Task marked as done

---

List All Tasks

python task_cli.py list

---

List Todo Tasks

python task_cli.py list todo

---

List In Progress Tasks

python task_cli.py list in-progress

---

List Done Tasks

python task_cli.py list done

---

Task Object Structure

{
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2026-06-09 10:30:00",
    "updatedAt": "2026-06-09 10:30:00"
}

---

Error Handling

The application handles:

- Missing Commands
- Missing Arguments
- Invalid Task IDs
- Non-Existing Tasks
- Empty Task Lists

---

Future Improvements

- Task Priority (Low, Medium, High)
- Due Dates
- Search Tasks
- Task Categories
- Colorized Terminal Output
- Unit Testing with Pytest
- Argparse-based CLI

---

Author

Hareesh

Python CLI Project for practicing:

- File Handling
- JSON Processing
- Exception Handling
- CRUD Operations
- Command Line Programming