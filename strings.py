name = "PyBan"
version = "0.1"
help = """
Pyban help:

help        Shows this help file.
version     Shows the version number.

boards      Lists the available kanban boards.
addboard    Adds a new board.
use [n]     Makes board n the active board.
            n can be gotten from the boards command.

show        Prints the active board.
name        Changes the name of the active board.
"""

format_use = "use [board number]"

format_name = "name [new board name]"

format_add = """
add board [board name]
add col [column name]
add task [task name]"""

format_del = """
del board [board number]
del col [col number]
del task ###############"""
