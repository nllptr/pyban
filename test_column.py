#!/bin/env python3

from pyban import Board, Column, Task
import unittest

class TestPyBanColumn(unittest.TestCase):
    """
    This test case tests the Column class of pyban.
    """

    def test_new_column(self):
        test_column = Column()
        self.assertEqual(test_column.get_name(), "New Column")

    def test_new_named_colum(self):
        test_column = Column("Test column")
        self.assertEqual(test_column.get_name(), "Test column")

    def test_set_name(self):
        test_column = Column()
        test_column.set_name("Name set")
        self.assertEqual(test_column.get_name(), "Name set")

    def test_set_description(self):
        test_column = Column()
        test_column.set_description("Desc set")
        self.assertEqual(test_column.get_description(), "Desc set")

    def test_add_task(self):
        test_column = Column()
        test_task = Task("Task1")
        self.assertTrue(test_column.add_task(test_task))

    def test_get_tasks(self):
        test_column = Column()
        task1 = Task("Task1")
        task2 = Task("Task2")
        test_column.add_task(task1)
        test_column.add_task(task2)
        task_list = test_column.get_tasks()
        self.assertEqual(2, len(task_list))

    def test_remove_task(self):
        test_column = Column()
        task1 = Task("Task1")
        task2 = Task("Task2")
        test_column.add_task(task1)
        test_column.add_task(task2)
        test_column.remove_task(1)
        task_list = test_column.get_tasks()
        self.assertEqual(1, len(task_list))

    def test_set_sub_board(self):
        test_column = Column()
        sub_board = Board()
        test_column.set_sub_board(sub_board)
        self.assertEqual(sub_board, test_column.get_sub_board())

    def test_clear_sub_board(self):
        test_column = Column()
        sub_board = Board()
        test_column.set_sub_board(sub_board)
        test_column.clear_sub_board()
        self.assertIsNone(test_column.get_sub_board())

if __name__ == "__main__":
    unittest.main()
