# MENU TEXT
MENU_TEXT = "Type '?' for help"

# DIALOG TEXTS
PROMPT_PROJECT_NAME = "Project name: "
PROMPT_NEW_BOARD = "Board name (default 'New Board'): "
PROMPT_BOARD_NAME = "Board name: "
PROMPT_BOARD_DESCRIPTION = "Board description: "
PROMPT_ADD_COLUMN = "Column name (default 'New Column'): "
PROMPT_COLUMN_NAME = "Column name: "
PROMPT_COLUMN_DESCRIPTION = "Column description: "
PROMPT_COLUMN_TASK_LIMIT = "Task limit: "
PROMPT_ADD_TASK = "Task name (default 'New Task'): "
PROMPT_TASK_NAME = "Task name: "
PROMPT_TASK_DESCRIPTION = "Task description: "

# INFO TEXTS
INFO_MOVE_COLUMN = "Move right or left?"
INFO_MOVE_TASK = "Move right or left?"

# HELP TEXTS
# Help texts are limited to 70 characters wide and 100 lines high
HELP_BOARD = """BOARD VIEW HELP ('q' closes this window)

?           View this help
q           Quit PyBan
h/j/k/l     Navigate the board view. Arrow keys are also
            supported. Go to project settings screen.
a           Show settings screen for the currently selected
            element. Works on tasks, columns and the board
            heading. Add a task to the currently selected column.
x           Remove the currently selected task.
m           Move the currently selected task to the left or
            right. Use h/l for left/right.
p           Show project settings"""

HELP_TASK_SETTINGS = """TASK SETTINGS HELP ('q' closes this window)

?           View this help
q           Leave task settings
n           Set task name
d           Set task description"""

HELP_COLUMN_SETTINGS = """COLUMN SETTINGS HELP ('q' closes this window)

?           View this help
q           Leave column settings
n           Set column name
d           Set column description
l           Set column task limit"""

HELP_BOARD_SETTINGS = """BOARD SETTINGS HELP ('q' closes this window)

?           View this help
q           Leave board settings
n           Set board name
d           Set board description
a           Add new board
r           Remove board"""

HELP_PROJECT_SETTINGS = """PROJECT SETTING HELP ('q' closes this window)

?           View this help
q           Leave project settings
a           Add new board
b           Set active board
r           Remove board"""

name = "PyBan"

version = "0.3.0"
