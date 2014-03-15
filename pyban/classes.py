import pickle
import os

class InvalidDirectoryError(Exception):
    pass

class Project:

    def __init__(self, name):
        self.name = name
        self.boards = []
        self.active_board = None

    def save(self):
        """
        Saves the state of the board list to .pyban/.
        """
        if not os.path.isdir(".pyban"):
            os.mkdir(".pyban")
        with open(".pyban/pyban.pk", "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        """
        Loads a saved board list from .pyban/ and
        returns True. Returns False if there is no project
        to load.
        """
        if not os.path.isdir(".pyban"):
            return False
        else:
            with open(".pyban/pyban.pk", "rb") as f:
                loaded = pickle.load(f)
                self.name = loaded.name
                self.boards = loaded.boards
                self.active_board = loaded.active_board
            return True

    def get_active(self):
        """
        Returns the active board or None if there
        is no active board.
        """
        if self.active_board == None:
            return None
        else:
            return self.boards[self.active_board]

    def __repr__(self):
        return "".join(["<Board: [name: ",
                        self.name,
                        "], [boards: ",
                        str(self.boards),
                        "], [active_board: ",
                        str(self.active_board),
                        "]>"])

    def __str__(self):
        return self.name

class Board:

    def __init__(self, name="New Board", description="<No description set>"):
        self.name = name
        self.description = description
        self.columns = []
        self.columns.append(Column("To do"))
        self.columns.append(Column("Doing"))
        self.columns.append(Column("Done"))

    def __repr__(self):
        return "".join(["<Board: [name: ",
                        self.name,
                        "], [description: ",
                        self.description,
                        "], [columns: ",
                        self.columns,
                        "]>"])

    def __str__(self):
        return ": ".join([self.name, self.description])

    def switch_columns(self, index1, index2):
        """
        Switches the positions of the columns with indices [index1]
        and [index2].
        """
        self.columns[index1], self.columns[index2] = self.columns[index2], self.columns[index1]

    def move_task(self, from_column, from_row, to_column):
        """
        Moves the task at [from_column], [from_row] to column [to_column].
        """
        if len(to_column.tasks) == to_column.max_simultaneous:
            return False
        else:
            self.columns[to_column].tasks.append(self.columns[from_column].tasks.pop(from_row))
            return True

class Column:

    def __init__(self, name="New Column", description="<No description set>"):
        self.name = name
        self.description = description
        self.tasks = []
        self.sub_board = None
        self.task_limit = 0

    def __repr__(self):
        return "".join(["<Column: [name: ",
                        self.name,
                        "], [description: ",
                        self.description,
                        "], [tasks: ",
                        str(self.tasks),
                        "], [sub_board: ",
                        str(self.sub_board),
                        "]>"])

    def __str__(self):
        return ": ".join([self.name, self.description])

class Task:

    def __init__(self, name="New Task", description="<No description set>"):
        self.name = name
        self.description = description

    def __repr__(self):
        return "".join(["<Task: [name: ",
                        self.name,
                        "], [description: ",
                        self.description,
                        "]>"])

    def __str__(self):
        return ": ".join([self.name, self.description])
