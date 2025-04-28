import unittest
import os
import json
from task_manager.core import add_task, load_tasks, delete_task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        os.environ["TASKS_FILE_PATH"] = self.test_file
        # S'assurer que le fichier de test est vide
        with open(self.test_file, 'w') as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task_id = add_task("Test task", 1)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertEqual(tasks[0]["priority"], 1)
        self.assertEqual(tasks[0]["id"], task_id)

    def test_delete_task(self):
        add_task("Task to delete", 2)
        self.assertTrue(delete_task(1))
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertFalse(delete_task(1))

if __name__ == "__main__":
    unittest.main() 