import pickle
import os

class InvalidDirectoryError(Exception):
    pass

class Project:

    def __init__(self, project_name):
#        if not path.isdir(project_dir):
#            raise InvalidDirectoryError
#        self.project_dir = project_dir
        self.project_name = project_name
        self.boards = []
        self.active_board = None

    def save(self):
        """
        Saves the state of the board list to [project_dir]
        """
        if not os.path.isdir(".pyban"):
            os.mkdir(".pyban")
        with open(".pyban/pyban.pk", "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        """
        Loads a saved board list from [project_dir] and
        returns True. Returns False if there is no project
        to load.
        """
        if not os.path.isdir(".pyban"):
            return False
        else:
            with open(".pyban/pyban.pk", "rb") as f:
                loaded = pickle.load(f)
                self.project_name = loaded.project_name
                self.boards = loaded.boards
                self.active_board = loaded.active_board
            return True

    def __repr__(self):
        return "<Board: [project_name: " + self.project_name \
            + "], [boards: " + str(self.boards) \
            + "], [active_board: " + str(self.active_board) \
            + "]>"

    def __str__(self):
        return self.project_name

class Board:

    def __init__(self, name="New Board", description="<No description set>"):
        self.name = name
        self.description = description
        self.columns = []
        self.columns.append(Column("To do"))
        self.columns.append(Column("Doing"))
        self.columns.append(Column("Done"))

    def __repr__(self):
        return "<Board: [name: " + self.name \
            + "], [description: " + self.description \
            + "], [columns: " + self.columns \
            + "]>"

    def __str__(self):
        return self.name + ": " + self.description

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
        self.columns[to_column].tasks.append(self.columns[from_column].tasks.pop(from_row))

class Column:

    def __init__(self, name="New Column", description="<No description set>"):
        self.name = name
        self.description = description
        self.tasks = []
        self.sub_board = None

    def __repr__(self):
        return "<Column: [name: " + self.name \
        + "], [description: " + self.description \
        + "], [tasks: " + str(self.tasks) \
        + "], [sub_board: " + str(self.sub_board) \
        + "]>"

    def __str__(self):
        return self.name + ": " + self.description

class Task:

    def __init__(self, name="New Task", description="<No description set>"):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Task: [name: " + self.name \
            + "], [description: " + self.description \
            + "]>"

    def __str__(self):
        return self.name + ": " + self.description
