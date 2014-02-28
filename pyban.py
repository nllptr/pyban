#!/bin/env python3

import pickle
import os

class PyBanException(BaseException): pass
class BoardException(PyBanException): pass
class ColumnException(PyBanException): pass
class TaskException(PyBanException): pass

class BoardList:
    def __init__(self):
        self.boards = []
        self.active_board = None

    def __repr__(self):
        return str(self.boards)

    def __str__(self):
        return self.__repr__()

    def add_board(self):
        self.boards.append(Board())

    def save(self):
        directory = os.path.expanduser("~") + "/.pyban"
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        with open(directory + "/boards.pk", "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        directory = os.path.expanduser("~") + "/.pyban"
        try:
            with open(directory + "/boards.pk", "rb") as f:
                loaded = pickle.load(f)
                self.boards = loaded.boards
                self.active_board = loaded.active_board
        except FileNotFoundError:
            try:
                os.mkdir(os.path.expanduser("~") + "/.pyban")
            except FileExistsError:
                pass
            return self

    def get_board_list(self):
        return self.boards

    def add_board(self, name="New Board"):
        self.boards.append(Board(name))

    def set_active(self, index):
        self.active_board = self.boards[index]

    def get_active(self):
        if self.active_board == None:
            return None
        else:
            return self.active_board

class Board:

    def __init__(self, name="New Board"):
        self.name = name
        self.description = "<Description not set>"
        self.columns = []
        self.columns.append(Column("To do"))
        self.columns.append(Column("Doing"))
        self.columns.append(Column("Done"))

    def __repr__(self):
        return "[" + self.name + ": " + self.description + "]"

    def __str__(self):
        return self.__repr__()

    def save(self):
        directory = os.getcwd() + "/.pyban"
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        with open(".pyban/board.pk", "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open(".pyban/board.pk", "rb") as f:
            loaded = pickle.load(f)
            self.name = loaded.get_name()
            self.description = loaded.get_description()
            self.columns = loaded.get_columns()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def add_column(self, index, column):
        return_value = False
        if isinstance(column, Column):
            return_value = True
            self.columns.insert(index, column)
        return return_value

    def remove_column(self, index):
        self.columns.pop(index)

    def switch_columns(self, index1, index2):
        tmp = self.columns[index1]
        self.columns[index1] = self.columns[index2]
        self.columns[index2] = tmp

    def get_column(self, index):
        return self.columns[index]

    def get_columns(self):
        return self.columns

class Column:

    def __init__(self, name="New Column"):
        self.name = name
        self.description = "<No description set>"
        self.tasks = []
        self.sub_board = None

    def __repr__(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        return_value = False
        if isinstance(task, Task):
            return_value = True
            self.tasks.append(task)
        return return_value

    def remove_task(self, index):
        return_task = None
        if index < len(self.tasks):
            return_task = self.tasks.pop(index)
        return return_task

    def get_sub_board(self):
        return self.sub_board

    def set_sub_board(self, board):
        self.sub_board = board

    def clear_sub_board(self):
        self.sub_board = None

class Task:

    def __init__(self, name="New Task"):
        self.name = name
        self.description = "<No description set>"

    def __repr__(self):
        pass

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
