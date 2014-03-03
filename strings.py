name = "PyBan"

version = "0.1"

unknown_command = "Unknown command. Type \"help\" to see all commands."

full_help = """
Pyban help:

help
Shows this help file.

version
Shows the version number.

use <integer>
Make board <integer> the active board. Use without the parameter to get a list of available board numbers.

add board <string>
Adds a new board to the board list. The new board will have the name <string> if it is provided, "New Board" otherwise.

add col <integer> <name>
Adds a new column to the active board.
<integer> is required and is the place where the column should be inserted, starting from 1.
<name> is the optional column name. If left out, a default value will be used.


add [board|col|task] <string>
Adds a new board, column or task and gives it the provided name. To add a new column or task, an active board must be set (see the "use" command). If no name is provided, a default name will be set.

show
Prints the active board.

board set [name|desc] <string>
Sets the active board's name or description to the provided value.

col set [name|desc|sub] <column number> <name|description>
Sets the name, description or, sub board of the column.
name and desc options expect strings, while sub expects a board number.
"""

format_use = "use [board number]"

format_name = "name [new board name]"

format_add = "add [board|col|task] <name>"

format_del = "del [board|col|task] <integer>"

format_del_board = "del board <board>"

format_del_col = "del col <column>"

format_del_task = "del task <column> <row>"

format_board = "board set [name|desc] <string>"

format_col = "col set [name|desc|sub] <column> <string>"

format_col_set_name = "col set <column> <name>"

format_col_set_desc = "col set <column> <description>"

format_show = "show | show <col> | show <col> <row>"

format_show_col = "show <col>"

format_show_task = "show <col> <row>"

format_move = "move <from column> <task number> <to column>"
