import os
import json

class Config:
    def __init__(self):
        self.tasks_file = os.getenv("TASKS_FILE_PATH", "tasks.json")
        self.log_file = os.getenv("LOG_FILE_PATH", "task_manager.log")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

    def load_config(self):
        """Charge la configuration depuis un fichier JSON si disponible."""
        config_file = os.getenv("CONFIG_FILE", "config.json")
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config_data = json.load(f)
                self.tasks_file = config_data.get("tasks_file", self.tasks_file)
                self.log_file = config_data.get("log_file", self.log_file)
                self.log_level = config_data.get("log_level", self.log_level)

    def save_config(self):
        """Sauvegarde la configuration dans un fichier JSON."""
        config_file = os.getenv("CONFIG_FILE", "config.json")
        config_data = {
            "tasks_file": self.tasks_file,
            "log_file": self.log_file,
            "log_level": self.log_level
        }
        with open(config_file, 'w') as f:
            json.dump(config_data, f, indent=4) 