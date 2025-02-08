# Template.py is a starter script that helps set up your Data Science project automatically. Instead of manually creating folders and 
# files, this script does it for you.
"""
import os

# List of folders to create
folders = ["data", "notebooks", "models", "src", "logs"]

# Create folders if they don't exist
for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Project structure created successfully!")
"""


import os
from pathlib import Path
import logging


logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s')

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep"                #gitkeep helps toautomate deployment
    f"{project_name}/__init__.py",              #__init__.py  marks a folder as a Python package, use of this constructor is we can use any modules used
    # in this project anywhere
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb"
    "templates/index.html"
]


for file_path in list_of_files:
    filepath = Path(file_path)        # just taking the file name from the list but implimenting "Path" can be compatible to Mac os/Windows/Linux
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)  #exist_ok=True prevents errors if the folder already exists.

    # what happening here is if filedir is not empty means having files inside that folder or directory so 1st we should create folder then should create files in it
        logging.info(f"Creating Directory {filedir} for {filename} was done")

    if ( not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,'w') as f:
            pass
            logging.info(f"creating an empty file {filepath}")
    else:
        logging.info("f{filename} is already exists")



