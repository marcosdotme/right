from cleo.application import Application
from right.console.commands import COMMANDS


cli = Application(name = 'Right', version = '0.1.0')
for command in COMMANDS:
    cli.add(command)
