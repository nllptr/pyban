#!/bin/env python3

from pyban import Board, Column, Task
import unittest

class TestPyBanBoard(unittest.TestCase):
    """
    This test case tests the Column class of pyban.
    """

    def test_new_board(self):
        test_board = Board()
        self.assertEqual(test_board.get_name(), "New Board")

    def test_new_named_board(self):
        test_board = Board("Test board")
        self.assertEqual("Test board", test_board.get_name())

    def test_set_name(self):
        test_board = Board()
        test_board.set_name("Name set")
        self.assertEqual("Name set", test_board.get_name())

    def test_set_description(self):
        test_board = Board()
        test_board.set_description("Description set")
        self.assertEqual("Description set", test_board.get_description())

    def test_add_column(self):
        test_board = Board()
        new_column = Column()
        test_board.add_column(1, new_column)
        self.assertIs(new_column, test_board.get_column(1))

    def test_remove_columns(self):
        test_board = Board()
        test_board.remove_column(2)
        self.assertEqual(2, len(test_board.get_columns()))

    def test_switch_columns(self):
        test_board = Board()
        test_board.switch_columns(0, 1)
        self.assertEqual("To do", test_board.get_column(1).get_name())

    def test_save_load_board(self):
        test_board = Board()
        test_board.get_column(1).set_name("changed")
        test_board.save()
        load_board = Board()
        load_board.load()
        self.assertEqual("changed", load_board.get_column(1).get_name())

if __name__ == "__main__":
    unittest.main()
