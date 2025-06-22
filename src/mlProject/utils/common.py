"""
Utils: Utils are utility functions for the test suite.
lets say you want to read the yaml file in all of our components, 
so instead of writing the yaml read function in all the files you can keep it inside common.py file.
so whenever you want to read the yaml file, you can import the common.py file and use the function.
"""

"""
ConfigBox : The purpose of config box is to convert the data into class attributes instead of keeping it as a dictionary/ some other data structure.
for example, if you have a dictionary like {'a': 1, 'b': 2}, with a normal dictionary, you can only access the value of 'a' using dict['a'].
but with config box, you can access the value of 'a' using dict.a.

Example code snippet:
from box import ConfigBox
d = {'a': 1, 'b': 2}
print(d.a)                  ### this will raise an error
config = ConfigBox({'a': 1, 'b': 2})   ### this will convert the dictionary into class attributes
print(config.a)  # Output: 1
"""

"""
Ensure Annotations: Ensure annotations is a decorator that ensures that the function has type annotations.
It is used to ensure that the function has type annotations and that the types are correct.
in the below example, though the function add has type mentioned in it as int, 
it will not raise an error if the types are not correct(even if you pass a string it will work).
To overcome this, we can use ensure annotations decorator which will raise an error if the types are not correct.

Example code snippet:
from ensure import ensure_annotations
@ensure_annotations
def add(a: int, b: int) -> int:
    return a + b
add(1, 2)  # Output: 3
add(1, "2")  # Raises TypeError: Expected type 'int' for argument 'b', got 'str' instead. 
             # This error will come only if you use ensure annotations decorator.
"""



import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"




