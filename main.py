# main.py
import json

class Task:
    def __init__(self, title, description, category, due_date=None, priority=None, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} ({self.category})"

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return [Task(**task) for task in json.load(f)]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter task priority (low, medium, high): ")

    tasks.append(Task(title, description, category, due_date, priority))
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(task)

def edit_task(tasks):
    task_index = int(input("Enter task index to edit: "))
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        print(f"Editing task: {task}")
        task.title = input("Enter new title (or press Enter to keep current): ") or task.title
        task.description = input("Enter new description (or press Enter to keep current): ") or task.description
        task.category = input("Enter new category (or press Enter to keep current): ") or task.category
        due_date = input("Enter new due date (YYYY-MM-DD, or press Enter to keep current): ")
        if due_date:
            task.due_date = due_date
        priority = input("Enter new priority (low, medium, high, or press Enter to keep current): ")
        if priority:
            task.priority = priority
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def delete_task(tasks):
    task_index = int(input("Enter task index to delete: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def mark_task_completed(tasks):
    task_index = int(input("Enter task index to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_completed()
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark task as completed")
        print("6. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            edit_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            mark_task_completed(tasks)
        elif choice == 6:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

