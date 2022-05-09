from cleo.commands.command import Command
from cleo.helpers import option
from pathlib import Path

from right.utils.functions import create_directory, create_dunder_init_file


class InitCommand(Command):
    """
    Creates a <comment>Python Project Environment</> in the current directory.

    init
    """

    options = [
        option('name', None, 'Name of the project.', flag = False)
    ]

    help = '''\
Creates a <comment>Python Project Environment</> in the current directory.
'''

    def handle(self):
        name = self.option('name')

        if not name:
            name = Path.cwd().name.lower()

        question = self.create_question(
            f'Project name [<comment>{name}</comment>]: ',
            default = name
        )

        name = self.ask(question)
        
        directories = [
            'docs',
            'tests',
            'assets',
            'scripts',
            name
        ]

        for dir in directories:
            create_directory(dir = dir)
            create_dunder_init_file(dir = dir)

        self.line(f'Your project name is: `{name}`')
