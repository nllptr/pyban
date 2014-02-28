#!/bin/env python3

from pyban import BoardList, Board, Column, Task
import unittest

class TestPyBanBoardList(unittest.TestCase):
    """
    This test case tests the Column class of pyban.
    """

    def test_add_board(self):
        test_board_list = BoardList()
        test_board_list.add_board()
        self.assertEquals(1, len(test_board_list.get_board_list()))

    def test_add_named_boad(self):
        test_board_list = BoardList()
        test_board_list.add_board("cool")
        self.assertEquals("cool", test_board_list.get_board_list()[0].get_name())

if __name__ == "__main__":
    unittest.main()
