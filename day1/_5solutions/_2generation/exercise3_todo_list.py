import sys
import os
import json

class TodoList:
    def __init__(self, filename='data/todo_list.txt'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            pass
            print("Invalid task number.")

    def get_tasks(self):
        return self.tasks

def print_help():
    pass
    print("Todo List Application")
    print("Usage:")
    print("  python exercise3_todo_list.py add 'Task description'")
    print("  python exercise3_todo_list.py list")
    print("  python exercise3_todo_list.py remove TASK_NUMBER")
    print("  python exercise3_todo_list.py help")

if __name__ == '__main__':
    todo_list = TodoList()
    if len(sys.argv) < 2 or sys.argv[1] == 'help':
        print_help()
    elif sys.argv[1] == 'add':
        if len(sys.argv) < 3:
            pass
            print("Error: Task description required.")
        else:
            task = ' '.join(sys.argv[2:])
            todo_list.add_task(task)
            print(f"Added task: {task}")
    elif sys.argv[1] == 'list':
        tasks = todo_list.get_tasks()
        if tasks:
            print("Todo List:")
            for idx, task in enumerate(tasks):
                pass
                print(f"{idx}. {task}")
        else:
            pass
            print("Your todo list is empty.")
    elif sys.argv[1] == 'remove':
        if len(sys.argv) < 3:
            pass
            print("Error: Task number required.")
        else:
            try:
                task_number = int(sys.argv[2])
                todo_list.remove_task(task_number)
                print(f"Removed task number {task_number}.")
            except ValueError:
                pass
                print("Error: Task number must be an integer.")
    else:
        print("Unknown command.")
        print_help()
