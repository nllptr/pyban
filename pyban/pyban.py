#!/bin/env python3

import curses

from classes import Project, Board, Column, Task
import constants
import strings

def main(stdscr):
    project = Project("New Project")
    project.load()

    state = constants.PROJECT_INFO
    curses.curs_set(False)

    while True:
        stdscr.clear()


        ##############################
        # States                     #
        ############################## 
        # Project info

        if state == constants.PROJECT_INFO:
            print_project_info(stdscr, project)
            print_menu(stdscr, strings.MENU_PROJECT_INFO)

        elif state == constants.SET_PROJECT_NAME:
            print_project_info(stdscr, project)
            name = get_input(stdscr, strings.SET_PROJECT_NAME)
            if len(name) > 0:
                project.project_name = name
                project.save()
            state = constants.PROJECT_INFO
            continue

        elif state == constants.NEW_BOARD:
            print_project_info(stdscr, project)
            name = get_input(stdscr, strings.NEW_BOARD)
            if len(name) > 0:
                project.boards.append(Board(name))
            else:
                project.boards.append(Board())
            project.save()
            state = constants.PROJECT_INFO
            continue

        elif state == constants.SET_ACTIVE_BOARD:
            select_board(stdscr, project)
            project.save()
            state = constants.PROJECT_INFO
            continue

        ##############################
        # Board view
        elif state == constants.BOARD:
            if project.active_board is None:
                state = constants.PROJECT_INFO
                continue
            else:
                state = print_board(stdscr, project)
            

        ############################## 
        # Command input              #
        ############################## 

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("q"):
            break
        elif state == constants.PROJECT_INFO:
            if key == ord("b"):
                state = constants.NEW_BOARD
            elif key == ord("a"):
                state = constants.SET_ACTIVE_BOARD
            elif key == ord("n"):
                state = constants.SET_PROJECT_NAME
            elif key == ord(" "):
                state = constants.BOARD
        elif state == constants.BOARD:
            if key == ord(" "):
                state = constants.PROJECT_INFO

def get_input(stdscr, message):
    """
    Shows the input line and takes input. The input must be
    decoded, or else a bytestring is returned.
    """
    max_yx = stdscr.getmaxyx()
    stdscr.addstr(max_yx[0] - 2, 1, message)
    curses.curs_set(True)
    curses.echo()
    input_string = stdscr.getstr(max_yx[0] - 2, 1 + len(message))
    curses.noecho()
    curses.curs_set(False)
    return input_string.decode()

def print_board(stdscr, project):
    """
    Prints the active board.
    """
    board = project.boards[project.active_board]
    max_yx = stdscr.getmaxyx()
    width_without_vlines = max_yx[1] - 1 - len(board.columns)
    columns = [width_without_vlines // len(board.columns)] * len(board.columns)
    remains = width_without_vlines % len(board.columns)
    counter = 0
    while remains > 0:
        columns[counter] += 1
        remains -= 1
        counter += 1
        if counter == 4:
            counter = 0

    # PRINT BOARD HEADER
    print_box(stdscr, 0, 0, ": ".join([project.project_name, board.name]))
    if len(board.columns) == 0:
        # print error message / go to create columns
        pass
    else:
        # PRINT COLUMN HEADERS
        stdscr.addch(3, 0, curses.ACS_ULCORNER)
        for column in columns:
            for i in range(column):
                stdscr.addch(curses.ACS_HLINE)
            stdscr.addch(curses.ACS_TTEE)
        stdscr.addch(curses.ACS_TTEE)
        stdscr.addch(3, max_yx[1] - 1, curses.ACS_URCORNER)
        stdscr.addch(curses.ACS_VLINE)
        for index, column in enumerate(columns):
            print_string = "".join([" ", board.columns[index].name, " "])
            if len(print_string) > column:
                print_string = print_string[:column]
            else:
                print_string = "".join([print_string, " " * (column - len(print_string))])
            stdscr.addstr(print_string)
            stdscr.addch(curses.ACS_VLINE)
        stdscr.addch(curses.ACS_LTEE)
        for column in columns:
            for i in range(column):
                stdscr.addch(curses.ACS_HLINE)
            stdscr.addch(curses.ACS_PLUS)
        stdscr.addch(5, max_yx[1] - 1, curses.ACS_RTEE)

def print_project_info(stdscr, project):
    """
    Prints the project info.
    """
    stdscr.addstr(1, 1, project.project_name)
    for index, board in enumerate(project.boards):
        if index == project.active_board:
            stdscr.addstr(index + 3, 2, "".join(["* ", str(project.boards[index])]))
        else:
            stdscr.addstr(index + 3, 2, "".join(["  ", str(project.boards[index])]))

def print_box(stdscr, y, x, print_string):
    """
    Prints a string inside a box with its upper left corners
    at the given coordinates.
    """
    stdscr.addch(y, x, curses.ACS_ULCORNER)
    print_chars = 1 + len(print_string) + 1
    for i in range(print_chars):
        stdscr.addch(curses.ACS_HLINE)
    stdscr.addch(curses.ACS_URCORNER)
    stdscr.addch(y + 1, 0, curses.ACS_VLINE)
    stdscr.addstr(y + 1, 2, print_string)
    stdscr.addstr(" ")
    stdscr.addch(curses.ACS_VLINE)
    stdscr.addch(y + 2, 0, curses.ACS_LLCORNER)
    for i in range(print_chars):
        stdscr.addch(curses.ACS_HLINE)
    stdscr.addch(curses.ACS_LRCORNER)

def print_menu(stdscr, menu):
    """
    Prints a menu. Menu texts are defined in strings.py.
    Menu definitions are lists of strings. One letter in each string
    is parenthesized. The parenthexised letter will be printed as underlined
    to indicate keyboard commands.
    """
    max_yx = stdscr.getmaxyx()
    offset = 0
    for item in menu:
        split_text = item.split("(")
        # If there is a split, split at the closing parenthesis as well.
        if len(split_text) > 1:
            split_text[1] = split_text[1].split(")")
        # If the first part is longer than 0, print it in normal text.
        if len(split_text[0]) > 0:
            stdscr.addstr(max_yx[0] - 1, 1 + offset, split_text[0])
        # Print the underlined part.
        stdscr.addstr(max_yx[0] - 1, 1 + offset + len(split_text[0]), split_text[1][0], curses.A_UNDERLINE)
        if len(split_text[1][1]) > 0:
            stdscr.addstr(max_yx[0] - 1, 1 + offset + len(split_text[0]) + len(split_text[1][0]), split_text[1][1])
        offset += len(item) + 3

def select_board(stdscr, project):
    """
    Prints the project info, but with the addition that the user
    is able to select one board with up/down keys or j/k and
    the enter key.
    """
    if project.active_board is None:
        selection = 0
    else:
        selection = project.active_board

    key = 0
    while key != 10:
        stdscr.clear()
        print_project_info(stdscr, project)
        print_menu(stdscr, strings.MENU_SELECT)
        stdscr.addstr(selection + 3, 4, str(project.boards[selection]), curses.A_REVERSE)
        key = stdscr.getch()
        if selection == 0:
            if key in (curses.KEY_DOWN, ord("j")):
                selection += 1
        elif selection == (len(project.boards) - 1):
            if key in (curses.KEY_UP, ord("k")):
                selection -= 1
        else:
            if key in (curses.KEY_DOWN, ord("j")):
                selection += 1
            if key in (curses.KEY_UP, ord("k")):
                selection -= 1
    project.active_board = selection


if __name__ == "__main__":
    curses.wrapper(main)
    
