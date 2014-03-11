#!/bin/env python3

import unittest

from classes import *

class TestTask(unittest.TestCase):
    """
    This class tests the Task class
    """

    def test_new_unnamed(self):
        task = Task()
        self.assertEqual("New Task", task.name)
        self.assertEqual("<No description set>", task.description)

    def test_new_named(self):
        task = Task("My task")
        self.assertEqual("My task", task.name)
        self.assertEqual("<No description set>", task.description)

    def test_new_desc(self):
        task = Task("Name", "Description")
        self.assertEqual("Name", task.name)
        self.assertEqual("Description", task.description)

    def test_str(self):
        test_string = "Task: Description"
        self.assertEqual(test_string, str(Task("Task", "Description")))

    def test_repr(self):
        test_string = "<Task: [name: New Task], [description: <No description set>]>"
        self.assertEqual(test_string, repr(Task()))

class TestColumn(unittest.TestCase):
    """
    This class tests the Column class
    """

    def test_new_unnamed(self):
        column = Column()
        self.assertEqual("New Column", column.name)
        self.assertEqual("<No description set>", column.description)

    def test_new_named(self):
        column = Column("Column")
        self.assertEqual("Column", column.name)
        self.assertEqual("<No description set>", column.description)
        self.assertEqual([], column.tasks)
        self.assertIsNone(column.sub_board)

    def test_new_desc(self):
        column = Column("Column", "Description")
        self.assertEqual("Column", column.name)
        self.assertEqual("Description", column.description)
        self.assertEqual([], column.tasks)
        self.assertIsNone(column.sub_board)

    def test_tasks(self):
        column = Column()
        column.tasks.append(Task(description="list-test"))
        self.assertEqual("list-test", column.tasks[0].description)

    def test_sub_board(self):
        column = Column()
        column.sub_board = Board("test-board")
        self.assertEqual("test-board", column.sub_board.name)

    def test_str(self):
        self.assertEqual("Column: Desc", str(Column("Column", "Desc")))

    def test_repr(self):
        test_string = "<Column: [name: New Column], [description: <No description set>], [tasks: []], [sub_board: None]>"
        self.assertEqual(test_string, repr(Column()))

class TestBoard(unittest.TestCase):
    """
    This class tests the Board class
    """

    def test_new_unnamed(self):
        board = Board()
        self.assertEqual("New Board", board.name)
        self.assertEqual("<No description set>", board.description)
        self.assertEqual("To do", board.columns[0].name)
        self.assertEqual("Doing", board.columns[1].name)
        self.assertEqual("Done", board.columns[2].name)

    def test_new_named(self):
        board = Board("Board")
        self.assertEqual("Board", board.name)

    def test_new_desc(self):
        board = Board("Board", "Desc")
        self.assertEqual("Board", board.name)
        self.assertEqual("Desc", board.description)

    def test_switch_columns(self):
        board = Board()
        board.switch_columns(0, 2)
        self.assertEqual("Done", board.columns[0].name)
        self.assertEqual("To do", board.columns[2].name)

    def test_move_task(self):
        board = Board()
        board.columns[0].tasks.append(Task("Hey"))
        board.move_task(0, 0, 1)
        self.assertEqual("Hey", board.columns[1].tasks[0].name)

class TestProject(unittest.TestCase):
    """
    This class tests the Project class
    """

    def test_new(self):
#        with self.assertRaises(InvalidDirectoryError):
#            Project("sdflksdjlkdf")
#        project1 = Project("/home/simon")
#        project2 = Project()
        project = Project("New project")
        self.assertEqual("New project", project.project_name)
        with self.assertRaises(TypeError):
            project = Project()

    def test_save_load(self):
        project = Project("test project")
        self.assertFalse(project.load(), "Make sure you delete the old .pyban folder")
        project.boards.append(Board("test board"))
        project.save()
        loaded = Project("new")
        self.assertTrue(loaded.load())
        self.assertEqual("test board", loaded.boards[0].name)

    def test_str(self):
        project = Project("new project")
        self.assertEqual("new project", str(project))

    def test_repr(self):
        project = Project("lol")
        repr_string = "<Board: [project_name: lol], [boards: []], [active_board: None]>"
        self.assertEqual(repr_string, repr(project))

if __name__ == "__main__":
    unittest.main()
