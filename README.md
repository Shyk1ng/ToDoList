# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows you to manage your tasks by adding, listing, completing, and removing them. The tasks are stored in a JSON file, so your data persists between runs of the program.

## Features

- **Add Task**: Add a new task to the to-do list.
- **List Tasks**: Display all tasks with their status (completed or not).
- **Complete Task**: Mark a task as completed.
- **Remove Task**: Remove a task from the list.

## Prerequisites

- Python 3.x

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/todo-list.git
    cd todo-list
    ```

2. **Run the application**:
    ```bash
    python todo.py
    ```

## Usage

When you run the application, you will see a menu with the following options:

1. Add task
2. Complete task
3. Remove task
4. Exit

### Adding a Task

To add a task, select option `1` and enter the task title when prompted.

### Listing Tasks

The tasks are automatically listed each time you perform an action. You can see the status of each task (✓ for completed, ✗ for not completed).

### Completing a Task

To complete a task, select option `2` and enter the task number you want to mark as completed.

### Removing a Task

To remove a task, select option `3` and enter the task number you want to remove.

### Exiting

To exit the application, select option `4`.

## Example

```text
To-Do List:
1. [✗] Buy groceries
2. [✗] Write blog post
3. [✓] Read a book

Options:
1. Add task
2. Complete task
3. Remove task
4. Exit

Enter your choice: 2
Enter task number to complete: 1
Task 'Buy groceries' marked as complete.
