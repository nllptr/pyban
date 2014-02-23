#!/bin/env python

import task

class Board:
    """
    A class descripbin a kanban board.
    """

    def __init__(self, columns=3):
        self._columns = columns
        self._column[columns] = {}

    def add_column(self):
        self._columns += 1

    def switch_columns(self, first_column, second_column):
        tmp = column[first_column]
        column[first_column] = column[second_column]
        column[second_column] = tmp
        
    def print_board(self):
        pass

if __name__ == "__main__":
    test_board = Board()
    print test_board._columns
