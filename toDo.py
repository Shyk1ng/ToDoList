import os
import json

TODO_FILE = 'todo_list.json'


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. [{status}] {task['title']}")


def add_task(tasks, title):
    tasks.append({'title': title, 'completed': False})
    print(f"Task '{title}' added.")


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print(f"Task '{tasks[index]['title']}' marked as complete.")
    else:
        print("Invalid task number.")


def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' removed.")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        list_tasks(tasks)
        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            add_task(tasks, title)
        elif choice == '2':
            try:
                index = int(input("Enter task number to complete: ").strip()) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: ").strip()) - 1
                remove_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        save_tasks(tasks)


if __name__ == "__main__":
    main()
