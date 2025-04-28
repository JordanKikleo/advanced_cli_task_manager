import json
import os
from task_manager.logger import setup_logger
from task_manager.config import Config

config = Config()
config.load_config()
logger = setup_logger()

def get_tasks_file():
    """Retourne le chemin du fichier de tâches en prenant en compte la variable d'environnement."""
    return os.getenv("TASKS_FILE_PATH", "tasks.json")

def load_tasks():
    tasks_file = get_tasks_file()
    if os.path.exists(tasks_file):
        try:
            with open(tasks_file, 'r') as f:
                content = f.read().strip()
                if not content:  # Si le fichier est vide
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            logger.warning(f"Invalid JSON in {tasks_file}, creating new empty file")
            return []
    return []

def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    # Vérifier si une tâche avec la même description existe déjà
    for task in tasks:
        if task["description"] == description:
            logger.warning(f"Task with description '{description}' already exists.")
            return task["id"]
    
    task_id = len(tasks) + 1
    task = {"id": task_id, "description": description, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Task added: {task}")
    return task_id

def list_tasks():
    tasks = load_tasks()
    logger.info("Tasks listed")
    return tasks

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            save_tasks(tasks)
            logger.info(f"Task deleted: {task}")
            return True
    logger.warning(f"Task with id {task_id} not found")
    return False 