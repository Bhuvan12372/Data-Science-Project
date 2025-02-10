import os
import json
from src.datascience import logger
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} file loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

"""In this code what we are doing mainly is whatever the yaml file we have, we have to read it or should import it in the code right 
so  opening yaml file can do in many files, so it is common for any file to use yaml file. so writing here can be easy to open it
and use in any file required.

Configbox what does is, yaml file means it is in dictionary right so it is normally like data = {Capital : {India : new Delhi, Andhra
pradesh : Amaravathi}}

so normal dictionary we will use like data['Capital']['India'] {new Delhi}

So now using ConfigBox, it will make much more easier 
data.Capital.India  {new delhi}, Go to jupyter notebook for a clearer idea of this
"""

@ensure_annotations
def create_directories(path_to_directories : list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok= True)
        if verbose:
            logger.info(f"created directory at {path}")
    

#In template.py created entire required high level structure for the project but while moving into code and after needed to create 
#more directories

@ensure_annotations
def save_json(path: Path, data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent = 4)

        logger.info(f"json file created at {path}")

@ensure_annotations
def save_bin(data, Any, path: Path):
    joblib.dump(value= data, filename= path)
    logger.info(f"Binary file saved at {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded at {path}")
    return data
