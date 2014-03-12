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
        #max_yx = stdscr.getmaxyx()


        ##############################
        # States                     #
        ############################## 
        # Project info

        if state == constants.PROJECT_INFO:
            print_project_info(stdscr, project)

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
            if project.active_board == None:
                state = constants.PROJECT_INFO
                continue
            else:
                state = print_board(stdscr, project)
                continue
            

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
            elif key == 27:
                state = constants.BOARD

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
    stdscr.addstr(1, 1, project.project_name + ": " + board.name)
    if len(board.columns) == 0:
        # print error message / go to create columns
        pass
    else:
        # print columns
        pass
    stdscr.getch()
    return constants.PROJECT_INFO

def print_project_info(stdscr, project):
    """
    Prints the project info.
    """
    stdscr.addstr(1, 1, project.project_name)
    for index, board in enumerate(project.boards):
        if index == project.active_board:
            stdscr.addstr(index + 3, 1, "* " + str(project.boards[index]))
        else:
            stdscr.addstr(index + 3, 1, "  " + str(project.boards[index]))
    print_menu(stdscr, strings.MENU_PROJECT_INFO)


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
        if len(split_text) > 1:
            split_text[1] = split_text[1].split(")")
        if len(split_text[0]) > 0:
            stdscr.addstr(max_yx[0] - 1, 1 + offset, split_text[0])
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
    if project.active_board == None:
        selection = 0
    else:
        selection = project.active_board
    print_project_info(stdscr, project)
    print_menu(stdscr, strings.MENU_SELECT)
    stdscr.addstr(selection + 3, 3, str(project.boards[selection]), curses.A_REVERSE)

    key = 0
    while key != 10:
        print_project_info(stdscr, project)
        stdscr.addstr(selection + 3, 3, str(project.boards[selection]), curses.A_REVERSE)
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
    
