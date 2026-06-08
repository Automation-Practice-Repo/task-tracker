import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
if not os.path.exists(FILE_NAME):
with open(FILE_NAME, "w") as file:
json.dump([], file)

with open(FILE_NAME, "r") as file:
    return json.load(file)

def save_tasks(tasks):
with open(FILE_NAME, "w") as file:
json.dump(tasks, file, indent=4)

def get_next_id(tasks):
if not tasks:
return 1
return max(task["id"] for task in tasks) + 1

def add_task(description):
tasks = load_tasks()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

task = {
    "id": get_next_id(tasks),
    "description": description,
    "status": "todo",
    "createdAt": current_time,
    "updatedAt": current_time
}

tasks.append(task)
save_tasks(tasks)

print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
tasks = load_tasks()

for task in tasks:
    if task["id"] == task_id:
        task["description"] = description
        task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_tasks(tasks)
        print("Task updated successfully")
        return

print("Task not found")

def delete_task(task_id):
tasks = load_tasks()

updated_tasks = [task for task in tasks if task["id"] != task_id]

if len(tasks) == len(updated_tasks):
    print("Task not found")
    return

save_tasks(updated_tasks)
print("Task deleted successfully")

def update_status(task_id, status):
tasks = load_tasks()

for task in tasks:
    if task["id"] == task_id:
        task["status"] = status
        task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_tasks(tasks)
        print(f"Task marked as {status}")
        return

print("Task not found")

def list_tasks(status=None):
tasks = load_tasks()

if status:
    tasks = [task for task in tasks if task["status"] == status]

if not tasks:
    print("No tasks found")
    return

print("-" * 120)

for task in tasks:
    print(
        f"ID: {task['id']} | "
        f"Description: {task['description']} | "
        f"Status: {task['status']} | "
        f"Created At: {task['createdAt']} | "
        f"Updated At: {task['updatedAt']}"
    )

print("-" * 120)

def main():
if len(sys.argv) < 2:
print("Please provide a command.")
return

command = sys.argv[1]

try:
    if command == "add":
        add_task(sys.argv[2])

    elif command == "update":
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        update_status(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        update_status(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print("Unknown command.")

except IndexError:
    print("Missing required arguments.")

except ValueError:
    print("Task ID must be an integer.")

if name == "main":
main()