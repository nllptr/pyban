# =====
# MENUS
# =====
#
# Menu texts are defined as a list of strings. The part of each string
# that should be underlined is put between parentheses.
#
# General menu items
# ------------------
QUIT = "(Q)uit"
PROJECT_SETTINGS = "(P)roject"

# Project Info
# ------------
SET_PROJECT_NAME = "Project (n)ame"
ADD_BOARD = "(A)dd board"
REMOVE_BOARD = "(R)emove board"
SET_ACTIVE = "Active (b)oard"
MENU_PROJECT_INFO = [SET_PROJECT_NAME, ADD_BOARD, REMOVE_BOARD, SET_ACTIVE, QUIT]

# Board Info
# ----------
SET_BOARD_NAME = "Board (n)ame"
SET_BOARD_DESCRIPTION = "Board (d)escription"
ADD_COLUMN = "(A)dd column"
REMOVE_COLUMN = "(R)emove column"
MENU_BOARD_INFO = [SET_BOARD_NAME, SET_BOARD_DESCRIPTION, ADD_COLUMN, REMOVE_COLUMN, QUIT]

# Column Info
# -----------
SET_COLUMN_NAME = "Column (n)ame"
SET_COLUMN_DESCRIPTION = "Column (d)escription"
SET_COLUMN_TASK_LIMIT = "Column task (l)imit"
MENU_COLUMN_INFO = [SET_COLUMN_NAME, SET_COLUMN_DESCRIPTION, SET_COLUMN_TASK_LIMIT, QUIT]

# Selection keys
# --------------
SELECT_UP = "Up (k)" # NOT USED
SELECT_DOWN = "Down[k]" # NOT USED
SELECT_CONFIRM = "Select()" # NOT USED
MENU_SELECT = ["j/k or arrow keys. Confirm with <Enter>"]

# Board
# -----
#MENU_BOARD = ["h/j/k/l or arrow keys. Make selection with <Space>"]
SELECT_BOARD_SETTINGS = "(S)ettings"
SELECT_BOARD = [SELECT_BOARD_SETTINGS, PROJECT_SETTINGS, QUIT]

SELECT_COLUMN_SETTINGS = "(S)ettings"
SELECT_COLUMN_MOVE = "(M)ove column"
SELECT_COLUMN = [SELECT_COLUMN_SETTINGS, SELECT_COLUMN_MOVE, PROJECT_SETTINGS, QUIT]

SELECT_TASK_SETTINGS = "(S)ettings"
SELECT_TASK_MOVE = "(M)ove task"
SELECT_TASK = [SELECT_TASK_SETTINGS, SELECT_TASK_MOVE, PROJECT_SETTINGS, QUIT]

MOVE_LEFT = "Left (h)"
MOVE_RIGHT = "Right (l)"
MENU_MOVE_TASK = [MOVE_LEFT, MOVE_RIGHT]

# DIALOG TEXTS
PROMPT_PROJECT_NAME = "Project name: "
PROMPT_NEW_BOARD = "Board name (default 'New Board'): "
PROMPT_BOARD_NAME = "Board name: "
PROMPT_BOARD_DESCRIPTION = "Board description: "
PROMPT_ADD_COLUMN = "Column name (default 'New Column'): "
PROMPT_COLUMN_NAME = "Column name: "
PROMPT_COLUMN_DESCRIPTION = "Column description: "
PROMPT_COLUMN_TASK_LIMIT = "Task limit: "
PROMPT_TASK_NAME = "Task name (defaule 'New Task'): "

# INFO TEXTS
INFO_MOVE_TASK = "Select destination column."

name = "PyBan"

version = "0.3.0"

unknown_command = "Unknown command. Type \"help\" to see all commands."

full_help = """
Pyban help:

help
Shows this help file.

version
Shows the version number.

use <integer>                       Make board <integer> the active board.
                                    Use without the parameter to get a list
                                    of available board numbers.

add board <string>                  Adds a new board to the board list. The
                                    new board will have the name <string> if
                                    it is provided, "New Board" otherwise.

add col <integer> <name>            Adds a new column to the active board.
                                    
                                    <integer> is required and is the place
                                    where the column should be inserted,
                                    starting from 1.

                                    <name> is the optional column name. If
                                    left out, a default value will be used.


add [board|col|task] <string>       Adds a new board, column or task and
                                    gives it the provided name. To add a
                                    new column or task, an active board must
                                    be set (see the "use" command). If no
                                    name is provided, a default name will
                                    be set.

show                                Prints the active board.

board set [name|desc] <string>      Sets the active board's name or
                                    description to the provided value.

col set [name|desc|sub] <column number> <name|description>
                                    Sets the name, description or, sub board
                                    of the column.

                                    <name> and <desc> options expect strings,
                                    while <sub> expects a board number.
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

format_task = "task set [name|desc] <column> <row> <name/description>"

format_task = "task set [name|desc] <column> <row> <name/description>"
