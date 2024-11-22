import json
import os
from datetime import datetime

# File path for storing the to-do list
TODO_FILE = 'todo_list.json'

def load_todo_list():
    """Load the to-do list from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

def save_todo_list(todo_list):
    """Save the to-do list to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file, indent=4)

def add_task(todo_list, task_name, priority, deadline=None):
    """Add a new task to the to-do list."""
    task = {
        'task': task_name,
        'priority': priority,
        'deadline': deadline,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'pending'
    }
    todo_list.append(task)
    save_todo_list(todo_list)

def display_tasks(todo_list):
    """Display all tasks in the to-do list."""
    if not todo_list:
        print("No tasks to display.")
        return

    print(f"\n{'Task':<30}{'Priority':<10}{'Deadline':<20}{'Status':<10}")
    print("-" * 80)

    for task in todo_list:
        print(f"{task['task']:<30}{task['priority']:<10}{task['deadline']:<20}{task['status']:<10}")

def mark_task_done(todo_list, task_name):
    """Mark a task as completed."""
    for task in todo_list:
        if task['task'].lower() == task_name.lower() and task['status'] == 'pending':
            task['status'] = 'completed'
            save_todo_list(todo_list)
            print(f"Task '{task_name}' marked as completed!")
            return
    print(f"Task '{task_name}' not found or already completed.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            priority = input("Enter priority (low, medium, high): ")
            deadline = input("Enter deadline (optional, YYYY-MM-DD): ")
            deadline = deadline if deadline else None
            add_task(todo_list, task_name, priority, deadline)
        elif choice == '2':
            display_tasks(todo_list)
        elif choice == '3':
            task_name = input("Enter task name to mark as done: ")
            mark_task_done(todo_list, task_name)
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
