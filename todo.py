import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def generate_new_id(tasks):
    """Generate a new ID based on existing tasks."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found. Add your first task!\n")
        return

    print("\nYour To-Do List:")
    print("-" * 40)
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'ID: {task["id"]} | [{status}] {task["title"]}')
    print("-" * 40 + "\n")


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    new_task = {
        "id": generate_new_id(tasks),
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def mark_completed(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("No tasks to update.")
        return

    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
            return

    print("Task ID not found.")


def edit_task(tasks):
    """Edit a task's title."""
    if not tasks:
        print("No tasks to edit.")
        return

    try:
        task_id = int(input("Enter task ID to edit: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            print(f"Current title: {task['title']}")
            new_title = input("Enter new title (leave blank to cancel): ").strip()
            if not new_title:
                print("Edit cancelled.")
                return
            task["title"] = new_title
            save_tasks(tasks)
            print("Task updated successfully!")
            return

    print("Task ID not found.")


def delete_task(tasks):
    """Delete a task."""
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task ID not found.")


def show_menu():
    """Display the main menu."""
    print("\n==== TO-DO LIST MENU ====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
