# Task Manager CLI

Un gestionnaire de tâches en ligne de commande avec des fonctionnalités avancées.

## Installation

### Création et activation de l'environnement virtuel

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur Linux/Mac :
source venv/bin/activate
```

### Installation du package

```bash
# Installer les dépendances
pip install -r requirements.txt

# Installer le package en mode développement
pip install -e .
```

## Utilisation

### Ajouter une tâche
```bash
python -m task_manager.cli add "Description de la tâche" 1
```
Le deuxième paramètre est la priorité (1-5).

### Lister les tâches
```bash
python -m task_manager.cli list
```

### Supprimer une tâche
```bash
python -m task_manager.cli delete 1
```
Le paramètre est l'ID de la tâche à supprimer.

## Configuration

Le gestionnaire de tâches utilise plusieurs variables d'environnement pour la configuration :

- `TASKS_FILE_PATH` : Chemin vers le fichier de stockage des tâches (par défaut : "tasks.json")
- `LOG_FILE_PATH` : Chemin vers le fichier de log (par défaut : "task_manager.log")
- `LOG_LEVEL` : Niveau de log (par défaut : "INFO")

## Tests

```bash
# Lancer tous les tests
python -m unittest discover tests

# Lancer un test spécifique
python -m unittest tests/test_core.py
```

## Structure du projet

```
advanced_cli_task_manager/
│── task_manager/          # Code source
│   │── __init__.py
│   │── cli.py            # Point d'entrée CLI
│   │── core.py           # Logique principale
│   │── logger.py         # Configuration des logs
│   │── config.py         # Gestion de la configuration
│── tests/                # Tests unitaires
│   │── test_core.py
│── tasks.json            # Fichier de stockage des tâches
│── requirements.txt      # Dépendances
│── README.md            # Documentation
```