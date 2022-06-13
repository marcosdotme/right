import platform
import subprocess
from pathlib import Path
from textwrap import dedent
from typing import Dict
from typing import List

from dulwich.config import ConfigFile


def create_directory(
    dir: str | List[str]
) -> None:
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


def create_dunder_init_file(
    dir: str | List[str]
) -> None:
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


def get_users_git_config(
    use_local_git_config: bool = True,
    use_global_git_config: bool = False
) -> Dict:
    """Reads the git configuration to get name and email for the current user.

    Keyword Arguments
    -----------------
        use_local_git_config `bool`: Uses local git configuration.
        use_global_git_config `bool`: Uses global git configuration.

    Returns
    -------
        `Dict`: Returns a dict with `name` and `email` keys.

    Example usage
    -------------
    >>> get_users_git_config()
    {'name': 'Your Name', 'email': 'your.email@your.domain.com'}
    """

    local_git_config_file = Path().cwd() / '.git/config'
    global_git_config_file = Path().home() / '.gitconfig'

    if use_local_git_config and local_git_config_file.exists():
        config_file = local_git_config_file

    if use_global_git_config and global_git_config_file.exists():
        config_file = global_git_config_file

    if not local_git_config_file.exists() and not global_git_config_file.exists():
        return {'name': None, 'email': None}

    with open(config_file, 'br') as file:
        dulwich_config_file = ConfigFile.from_file(file)

        try:
            name = dulwich_config_file.get(section = 'user', name = 'name').decode()
            email = dulwich_config_file.get(section = 'user', name = 'email').decode()
            return {'name': name, 'email': email}
        except KeyError:
            return {'name': None, 'email': None}


def git_is_installed(
) -> bool:
    """Checks if git is installed and configured in path.

    Returns
    -------
        `bool`: Returns boolean.

    Example usage
    -------------
    >>> print(git_is_installed())
    True
    """

    from rich import print

    try:
        subprocess.run(
            ['git', '--version'],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL
        )
        return True
    except FileNotFoundError:
        print(
            dedent('''\
        [bold red]Git is not installed or not in path. [/bold red]Check the link and install before proceed: [link=https://git-scm.com/]https://git-scm.com/[/link]''')
        )
        return False


def initiate_git(
) -> None:
    """Initiate a git repository and do a checkout to 'dev' branch.

    Example usage
    -------------
    >>> initiate_git()
    """

    subprocess.run(
        ['git', 'init', '-b', 'main'],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
    )
    subprocess.run(
        ['git', 'checkout', '-b', 'dev'],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
    )


def install_poetry(
) -> bool:
    """Installs Poetry.

    Returns
    -------
        `bool`: Returns boolean if Poetry has been installed.

    Example usage
    -------------
    >>> install_poetry()
    """

    from rich import print

    script = 'right/vendor/poetry/install-poetry.py'
    
    # Installs Poetry
    try:
        subprocess.run(
            ['python', script],
            stdout = subprocess.DEVNULL
        )
    except FileNotFoundError:
        try:
            subprocess.run(
                ['python3', script],
                stdout = subprocess.DEVNULL
            )
        except FileNotFoundError:
            print(
                dedent('''\
            [bold red]python or python3 is installed and configured in your path?[/bold red]''')
            )
            return False

    # Checks if Poetry where installed and configured in path
    try:
        subprocess.run(
            ['poetry', '--version'],
            stdout = subprocess.DEVNULL
        )
        return True
    except FileNotFoundError:
        print(
            dedent('''\
        [bold red]There's an error with Poetry install.[/bold red] Please try to install manually: [link=https://python-poetry.org/docs/#installation]https://python-poetry.org/docs/#installation[/link]''')
        )
        return False


def detect_os(
) -> str:
    """Returns the name of operating system.

    Returns
    -------
        `str`: 'Windows', 'Linux' or 'MacOS'.

    Example usage
    -------------
    >>> print(detect_os())
    'Windows'
    """

    if platform.system() == 'Darwin':
        return 'MacOS'
    
    # If it's any other operating system
    return platform.system()
