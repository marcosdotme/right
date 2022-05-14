from pathlib import Path

from cleo.commands.command import Command
from cleo.helpers import option
from right.utils.functions import create_directory
from right.utils.functions import create_dunder_init_file


class InitCommand(Command):
    name = 'init'

    description = (
        'Creates a <comment>Python Project Environment</> in the current directory.'
    )

    options = [
        option(
            long_name = 'name',
            description = 'Name of your project.',
            flag = False)
    ]

    help = '''
Creates a <comment>Python Project Environment</> in the current directory.

A <comment>Python Project Environment</> includes:
    - ...
    - ...
'''

    def handle(self):

        # This variable value is 'None'
        # if user doesn't explicitly pass the argument --name
        # on the command-line interface
        name = self.option('name')

        # The default value for variable 'name' will be
        # the name of the current directory if user doesn't
        # explicitly pass the argument --name on the command-line interface
        if not name:
            name = Path.cwd().name.lower()

        question = self.create_question(
            f'Project name [<comment>{name}</comment>]: '
        )

        # Prompts the question and get the value
        # passed by the user
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
