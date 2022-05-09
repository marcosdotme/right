from pathlib import Path
from typing import List, Union


def create_directory(dir: Union[str, List[str]]) -> None:
    """Creates a new directory in current directory.

    Arguments
    ---------
        dir `Union[str, List[str]]`: Directory to be created.

    Example usage
    -------------
    >>> create_directory(dir = ['one-folder', 'another-folder'])
    """

    if isinstance(dir, str):
        new_directory = Path.cwd() / dir
        new_directory.mkdir(exist_ok = True)

    if isinstance(dir, list):
        for directory in dir:
            new_directory = Path.cwd() / directory
            new_directory.mkdir(exist_ok = True)


def create_dunder_init_file(dir: Union[str, List[str]]) -> None:
    """Creates a __init__.py file inside the directory.

    Arguments
    ---------
        dir `Union[str, List[str]]`: Directory where the __init__.py file will be created.

    Example usage
    -------------
    >>> create_dunder_init_file(dir = ['one-folder', 'another-folder'])
    """

    if isinstance(dir, str):
        try:
            file = Path(dir) / '__init__.py'
            file.touch(exist_ok = True)
        except FileNotFoundError:
            print(f"Directory '{dir}' doesn't exists.")

    if isinstance(dir, list):
        for directory in dir:
            try:
                file = Path(directory) / '__init__.py'
                file.touch(exist_ok = True)
            except FileNotFoundError:
                print(f"Directory '{directory}' doesn't exists.")
