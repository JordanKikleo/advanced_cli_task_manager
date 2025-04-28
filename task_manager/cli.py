import argparse
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    add_parser.add_argument("priority", type=int, help="Task priority")

    # List Tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        task_id = add_task(args.description, args.priority)
        print(f"Task added with ID: {task_id}")
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}")
    elif args.command == "delete":
        if delete_task(args.task_id):
            print(f"Task {args.task_id} deleted successfully.")
        else:
            print(f"Task {args.task_id} not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 