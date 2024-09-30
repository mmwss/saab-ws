"""
Develop a command-line application that allows users to
add, list, and remove tasks from a todo list.
The tasks should be saved to a file so that they persist between runs in data/todo_list.json.
"""

import sys, os, json

def print_help():
    print("Usage:")
    print("  python day1/_2generation/exercise3_todo_list.py add 'Task description'")
    print("  python day1/_2generation/exercise3_todo_list.py list")
    print("  python day1/_2generation/exercise3_todo_list.py remove TASK_NUMBER")
    print("  python day1/_2generation/exercise3_todo_list.py help")

class TodoList:
    # Use AI code generation here
    pass  # Remove this pass statement after completing the code

# Example usage
if __name__ == "__main__":
    print("Code Generation[3] Todo List")

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

    print("Example usage:")
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Clean house")
    print(todo_list.get_tasks())
