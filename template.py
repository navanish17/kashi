import os, sys
import logging
from pathlib import Path

while True:
    project_name = input('Enter your project name: ')
    if project_name != "":
        break

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/research/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    'schema.yaml',
    'app.py',
    'main.py',
    'log.py',
    'exception.py',
    'setup.py'


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or os.path.getsize(filepath) ==0:
        with open(filepath, 'w')as f:
            pass

    else:
        logging.info('filepath already exists')   
