from pathlib import Path
from typing import Dict
from typing import List
from typing import Union

from dulwich.config import ConfigFile


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


def get_users_git_config(git_config_file: str = Path().home() / '.gitconfig') -> Dict:
    """Reads '.gitconfig' file to get name and email for the current user.

    Keyword Arguments
    -----------------
        git_config_file `str`: Path to '.gitconfig' file. (default = Path().home()/'.gitconfig')

    Returns
    -------
        `Dict`: Returns a dict with `name` and `email` keys.

    Example usage
    -------------
    >>> get_users_git_config()
    {'name': 'Your Name', 'email': 'your.email@your.domain.com'}
    """

    config_file = Path(git_config_file)

    if not config_file.exists():
        return {'name': '', 'email': ''}

    with open(config_file, 'br') as file:
        config_file = ConfigFile.from_file(file)

        try:
            name = config_file.get(section = 'user', name = 'name').decode()
            email = config_file.get(section = 'user', name = 'email').decode()
            return {'name': name, 'email': email}
        except KeyError:
            return {'name': '', 'email': ''}
