#!/bin/env python3

import pyban
import curses

def main(stdscr):

    menu_string = "Menu: Q = quit"

    running = True
    root_board = Board()
    columns = len(root_board.get_columns())
    column_width = 80 / columns

    while running:
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(0, 0, menu_string)

        mykey = stdscr.getch()
        if mykey == ord('q'):
            running = False

curses.wrapper(main)
