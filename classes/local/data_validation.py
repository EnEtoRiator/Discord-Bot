import os
from functools import wraps # Special decorator for wrappers at custom decorators for save meta data at input functions.
import re


path_pattern = r'^(?:[a-zA-Z]:)?[\\/]?(?:[\w\-\.]+[\\/])*[\w\-\.]+\.[a-zA-Z]{2,4}$'
"""
# RegEx
**Correct path examples:**
- `data/file.json`
- `C:\Users\doc.txt`
- `/var/log/app.log`
- `../images/photo.jpg`
- `my_report-v1.2.pdf`

**Features:**
- Supports spaces in names
- Allows parentheses () in names.
- Extensions up to 6 characters (for example .xlsx)
- Ignores paths ending in / (files only)
"""


    
def file_validate(_func: object):
    """
    # DECORATOR
    # Special file validator

    Args:
        _func (object):
        takes function under decorator.

    Raises:
        ValueError: Incorrect path pattern.
        ValueError: File doesn\'t exists

    Returns:
        function: After all checks call decorated function.
    
    Actually this decorator was made for fun as practice, i know what this is useless function.
    But some peoples can see how to work with decorators.
    """
    
    @wraps(_func) # read comment at imports!
    def wrapper(*args, **kwargs): # takes *args and **kwargs of input function
        
        hasMatches = False
        hasFile = False
        argMatch = ''
        
        for arg in args + tuple(kwargs.values()):
            
            if isinstance(arg, str):
                
                if re.match(path_pattern, arg):
                    hasMatches = True
                    argMatch = arg
                    if os.path.exists(arg):
                        hasFile = True
                    break
        
        if not hasMatches:
            raise ValueError(
                f"This function has incorrect arguments with pattern: \"{path_pattern}\"\nPresented arguments: \"{args+tuple(kwargs.values())}\"."
            )
        
        if not hasFile:
            raise ValueError(
                f"{_func.__name__}, called.\nLoaded file in path: \"{argMatch}\" doesn\'t exists!"
            )
        
        return _func(*args, **kwargs) # if all success, return result of called function with all coming arguments.
    return wrapper