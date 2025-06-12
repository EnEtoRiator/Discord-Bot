"""
# JSON I/O
file load/save system
"""
import json
from classes.local.data_validation import file_validate

@file_validate
def load(path: str) -> dict:
    """
    # JSON file loader

    Args:
        path (str): Takes path to file
        Absolute positional from main.py

    Returns:
        data (dict): Return python (dict) data type
    """
    return json.loads(open(f'{path}', 'r').read())

def save(path: str, data: dict) -> None:
    """
    # JSON file save

    Args:
        path (str): Takes (str) path to file.
        Absolute positional from main.py
        data (dict): Takes (dict) data to convert into json str and save it.
    """
    open(f'{path}', 'w').write(json.dumps(data))