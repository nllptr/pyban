#!/bin/env python3

import curses

from classes import Project, Board, Column, Task
import constants
import strings

def main(stdscr):
    project = Project("New Project")
    project.load()
    #
    # Create test project
    # -------------------
    #project.boards.append(Board("testing", "test description"))
    #project.boards[0].columns[0].tasks.append(Task("test task 1"))
    #project.boards[0].columns[0].tasks.append(Task("test task 2"))
    #project.boards[0].columns[1].tasks.append(Task("test task 3"))
    #project.boards[0].columns[2].tasks.append(Task("test task 4 this is a super duper mega long task name and i need to just to verify that task names are sliced correctly"))
    #project.boards[0].columns[2].tasks.append(Task("test task 5"))
    #project.boards[0].columns[2].tasks.append(Task("test task 6"))
    #project.active_board = 0

    state = constants.BOARD
    selection = [constants.BOARD_SELECT_BOARD, 0, 0]
    curses.curs_set(False)

    while True:
        stdscr.clear()


        # ======
        # States
        # ======
        # 
        # Project info
        # ------------
        if state == constants.PROJECT_INFO:
            print_project_info(stdscr, project)
            print_menu(stdscr, strings.MENU_PROJECT_INFO)
        elif state == constants.SET_PROJECT_NAME:
            print_project_info(stdscr, project)
            print_menu(stdscr, strings.MENU_PROJECT_INFO)
            name = get_input(stdscr, strings.PROMPT_PROJECT_NAME)
            if len(name) > 0:
                project.name = name
                project.save()
            state = constants.PROJECT_INFO
            continue
        elif state == constants.NEW_BOARD:
            print_project_info(stdscr, project)
            print_menu(stdscr, strings.MENU_PROJECT_INFO)
            name = get_input(stdscr, strings.PROMPT_NEW_BOARD)
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
        elif state == constants.REMOVE_BOARD:
            remove_board(stdscr, project)
            project.save()
            state = constants.PROJECT_INFO
            continue

        # Board info
        # ----------
        if state == constants.BOARD_INFO:
            print_board_info(stdscr, project)
            print_menu(stdscr, strings.MENU_BOARD_INFO)
        elif state == constants.SET_BOARD_NAME:
            print_board_info(stdscr, project)
            print_menu(stdscr, strings.MENU_BOARD_INFO)
            name = get_input(stdscr, strings.PROMPT_BOARD_NAME)
            if len(name) > 0:
                project.get_active().name = name
                project.save()
            state = constants.BOARD_INFO
            continue
        elif state == constants.SET_BOARD_DESCRIPTION:
            print_board_info(stdscr, project)
            print_menu(stdscr, strings.MENU_BOARD_INFO)
            description = get_input(stdscr, strings.PROMPT_BOARD_DESCRIPTION)
            if len(description) > 0:
                project.get_active().description = description
                project.save()
            state = constants.BOARD_INFO
            continue
        elif state == constants.ADD_COLUMN:
            print_board_info(stdscr, project)
            print_menu(stdscr, strings.MENU_BOARD_INFO)
            name = get_input(stdscr, strings.PROMPT_ADD_COLUMN)
            if len(name) > 0:
                project.get_active().columns.append(Column(name))
            else:
                project.get_active().columns.append(Column())
            project.save()
            state = constants.BOARD_INFO
            continue

        # Column info
        # -----------
        if state == constants.COLUMN_INFO:
            print_column_info(stdscr, project, selection)
            print_menu(stdscr, strings.MENU_COLUMN_INFO)
        elif state == constants.SET_COLUMN_NAME:
            print_column_info(stdscr, project, selection)
            print_menu(stdscr, strings.MENU_COLUMN_INFO)
            name = get_input(stdscr, strings.PROMPT_COLUMN_NAME)
            if len(name) > 0:
                project.get_active().columns[selection[1]].name = name
                project.save()
            state = constants.COLUMN_INFO
            continue
        elif state == constants.SET_COLUMN_DESCRIPTION:
            print_column_info(stdscr, project, selection)
            print_menu(stdscr, strings.MENU_COLUMN_INFO)
            description = get_input(stdscr, strings.PROMPT_COLUMN_DESCRIPTION)
            if len(description) > 0:
                project.get_active().columns[selection[1]].description = description
                project.save()
            state = constants.COLUMN_INFO
            continue
        elif state == constants.SET_COLUMN_TASK_LIMIT:
            print_column_info(stdscr, project, selection)
            print_menu(stdscr, strings.MENU_COLUMN_INFO)
            task_limit = get_input(stdscr, strings.PROMPT_COLUMN_TASK_LIMIT)
            if task_limit.isdigit():
                project.get_active().columns[selection[1]].task_limit = task_limit
                project.save()
            state = constants.COLUMN_INFO
            continue

        # Task info
        # ---------

        # Board view
        # ----------
        elif state == constants.BOARD:
            if project.get_active() is not None:
                print_board(stdscr, project, selection)
                if selection[0] == constants.BOARD_SELECT_BOARD:
                    print_menu(stdscr, strings.SELECT_BOARD)
                elif selection[0] == constants.BOARD_SELECT_COLUMN:
                    print_menu(stdscr, strings.SELECT_COLUMN)
                elif selection[0] == constants.BOARD_SELECT_TASK:
                    print_menu(stdscr, strings.SELECT_TASK)
            else:
                state = constants.PROJECT_INFO
                continue
        elif state == constants.ADD_TASK:
            print_board(stdscr, project, selection)
            if selection[0] == constants.BOARD_SELECT_COLUMN:
                print_menu(stdscr, strings.SELECT_COLUMN)
            elif selection[0] == constants.BOARD_SELECT_TASK:
                print_menu(stdscr, strings.SELECT_TASK)
            if len(project.get_active().columns[selection[1]].tasks) < int(project.get_active().columns[selection[1]].task_limit) or int(project.get_active().columns[selection[1]].task_limit) == 0:
                name = get_input(stdscr, strings.PROMPT_TASK_NAME)
                if len(name) > 0:
                    project.get_active().columns[selection[1]].tasks.append(Task(name))
                else:
                    project.get_active().columns[selection[1]].tasks.append(Task())
                project.save()
            else:
                # TODO: Task limit reached error
                pass
            state = constants.BOARD
            continue
        elif state == constants.REMOVE_TASK:
            project.get_active().columns[selection[1]].tasks.pop(selection[2])
            if selection[2] >= len(project.get_active().columns[selection[1]].tasks):
                selection[2] -= 1
            if selection[2] < 0:
                selection[2] = 0
                selection[0] = constants.BOARD_SELECT_COLUMN
            project.save()
            state = constants.BOARD
            continue
        elif state == constants.MOVE_TASK:
            print_board(stdscr, project, selection)
            print_info(stdscr, strings.INFO_MOVE_TASK)
            print_menu(stdscr, strings.MENU_MOVE_TASK)
            key = 0
            while key not in (ord("h"), ord("l")):
                key = stdscr.getch()
            if key == ord("h"):
                if selection[1] > 0:
                    if len(project.get_active().columns[selection[1] - 1].tasks) < int(project.get_active().columns[selection[1] - 1].task_limit) or project.get_active().columns[selection[1] - 1].task_limit == 0:
                        task = project.get_active().columns[selection[1]].tasks.pop(selection[2])
                        project.get_active().columns[selection[1] - 1].tasks.append(task)
            elif key == ord("l"):
                if selection[1] < (len(project.get_active().columns) - 1):
                    if len(project.get_active().columns[selection[1] + 1].tasks) < int(project.get_active().columns[selection[1] + 1].task_limit) or project.get_active().columns[selection[1] + 1].task_limit == 0:
                        task = project.get_active().columns[selection[1]].tasks.pop(selection[2])
                        project.get_active().columns[selection[1] + 1].tasks.append(task)
            project.save()
            state = constants.BOARD
            continue


        # ============= 
        # Command input
        # ============= 

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("!"):
            break
        elif state == constants.PROJECT_INFO:
            if key == ord("a"):
                state = constants.NEW_BOARD
            elif key == ord("b"):
                state = constants.SET_ACTIVE_BOARD
            elif key == ord("n"):
                state = constants.SET_PROJECT_NAME
            elif key == ord("r"):
                state = constants.REMOVE_BOARD
            elif key == ord("q"):
                state = constants.BOARD
        elif state == constants.BOARD_INFO:
            if key == ord("n"):
                state = constants.SET_BOARD_NAME
            elif key == ord("q"):
                state = constants.BOARD
            elif key == ord("d"):
                state = constants.SET_BOARD_DESCRIPTION
            elif key == ord("a"):
                state = constants.ADD_COLUMN
        elif state == constants.COLUMN_INFO:
            if key == ord("q"):
                state = constants.BOARD
            elif key == ord("n"):
                state = constants.SET_COLUMN_NAME
            elif key == ord("d"):
                state = constants.SET_COLUMN_DESCRIPTION
            elif key == ord("l"):
                state = constants.SET_COLUMN_TASK_LIMIT
        elif state == constants.BOARD:
            if key == ord("q"):
                break
            elif key == ord("p"):
                state = constants.PROJECT_INFO
            elif key == ord("s"):
                if selection[0] == constants.BOARD_SELECT_BOARD:
                    state = constants.BOARD_INFO
                elif selection[0] == constants.BOARD_SELECT_COLUMN:
                    state = constants.COLUMN_INFO
                elif selection[0] == constants.BOARD_SELECT_TASK:
                    state = constants.TASK_INFO
            elif key == ord("a"):
                if selection[0] != constants.BOARD_SELECT_BOARD:
                    state = constants.ADD_TASK
            elif key == ord("x"):
                if selection[0] == constants.BOARD_SELECT_TASK:
                    state = constants.REMOVE_TASK
            elif key == ord("m"):
                if selection[0] == constants.BOARD_SELECT_TASK:
                    state = constants.MOVE_TASK
            elif key in (ord("j"), curses.KEY_DOWN):
                if selection[0] == constants.BOARD_SELECT_BOARD:
                    selection = [constants.BOARD_SELECT_COLUMN, 0, 0]
                elif selection[0] == constants.BOARD_SELECT_COLUMN and len(project.get_active().columns[selection[1]].tasks) > 0:
                    selection[0] = constants.BOARD_SELECT_TASK
                    selection[2] = 0
                elif selection[0] == constants.BOARD_SELECT_TASK and selection[2] < len(project.get_active().columns[selection[1]].tasks) - 1:
                    selection[2] += 1
            elif key in (ord("k"), curses.KEY_UP):
                if selection[0] == constants.BOARD_SELECT_COLUMN:
                    selection = [constants.BOARD_SELECT_BOARD, 0, 0]
                elif selection[0] == constants.BOARD_SELECT_TASK:
                    if selection[2] > 0:
                        selection[2] -= 1
                    else:
                        selection[0] = constants.BOARD_SELECT_COLUMN
            elif key in (ord("l"), curses.KEY_RIGHT):
                if selection[0] != constants.BOARD_SELECT_BOARD:
                    if selection[1] < len(project.get_active().columns) - 1:
                        if selection[2] > len(project.get_active().columns[selection[1] + 1].tasks) - 1:
                            selection[2] = len(project.get_active().columns[selection[1] + 1].tasks) - 1
                        selection[1] += 1
            elif key in (ord("h"), curses.KEY_LEFT):
                if selection[0] != constants.BOARD_SELECT_BOARD:
                    if selection[1] > 0:
                        if selection[2] > len(project.get_active().columns[selection[1] - 1].tasks) - 1:
                            selection[2] = len(project.get_active().columns[selection[1] - 1].tasks) - 1
                        selection[1] -= 1

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

def print_info(stdscr, message):
    """
    Prints the provided message on the next to last line.
    """
    max_yx = stdscr.getmaxyx()
    stdscr.addstr(max_yx[0] - 2, 1, message)

def print_board(stdscr, project, selection):
    """
    Prints the active board.
    """
    board = project.get_active()
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

    # ==================
    # PRINT BOARD HEADER
    # ==================

    if selection[0] == constants.BOARD_SELECT_BOARD:
        print_box(stdscr, 0, 0, ": ".join([board.name, board.description]), curses.A_REVERSE)
    else:
        print_box(stdscr, 0, 0, ": ".join([board.name, board.description]))
    if len(board.columns) == 0:
        # print error message / go to create columns
        pass
    else:
        # PRINT COLUMN HEADERS
        stdscr.addch(3, 0, curses.ACS_ULCORNER)
        for index, column in enumerate(columns):
            for i in range(column):
                stdscr.addch(curses.ACS_HLINE)
            stdscr.addch(curses.ACS_TTEE)
        stdscr.addch(curses.ACS_TTEE)
        stdscr.addch(3, max_yx[1] - 1, curses.ACS_URCORNER)
        stdscr.addch(curses.ACS_VLINE)
        for index, column in enumerate(columns):
            if int(board.columns[index].task_limit) > 0:
                print_string = "".join([" [", board.columns[index].task_limit, "] ", board.columns[index].name])
            else:
                print_string = "".join([" ", board.columns[index].name])
            if len(print_string) > column:
                print_string = print_string[:column]
            else:
                print_string = "".join([print_string, " " * (column - len(print_string))])
            if selection[0] == constants.BOARD_SELECT_COLUMN:
                if selection[1] == index:
                    stdscr.addstr(print_string, curses.A_REVERSE)
                else:
                    stdscr.addstr(print_string)
            else:
                stdscr.addstr(print_string)
            stdscr.addch(curses.ACS_VLINE)
        stdscr.addch(curses.ACS_LTEE)
        for column in columns:
            for i in range(column):
                stdscr.addch(curses.ACS_HLINE)
            stdscr.addch(curses.ACS_PLUS)
        stdscr.addch(5, max_yx[1] - 1, curses.ACS_RTEE)


        # =============
        # PRINT COLUMNS
        # =============

        for i in range(max_yx[0] - 9):
            stdscr.addch(i + 6, 0, curses.ACS_VLINE)
            offset = 0
            for column in columns:
                offset += column + 1
                stdscr.addch(i + 6, offset, curses.ACS_VLINE)
        stdscr.addch(max_yx[0] - 3, 0, curses.ACS_LLCORNER)
        for column in columns:
            for i in range(column):
                stdscr.addch(curses.ACS_HLINE)
            stdscr.addch(curses.ACS_BTEE)
        stdscr.addch(max_yx[0] - 3, max_yx[1] - 1, curses.ACS_LRCORNER)


        # ===========
        # PRINT TASKS
        # ===========

        offset_y = 6
        offset_x = 1
        for column_index, column in enumerate(columns):
            stdscr.move(offset_y, offset_x)
            for task_index, task in enumerate(board.columns[column_index].tasks):
                if selection[0] == constants.BOARD_SELECT_TASK and selection[1] == column_index and selection[2] == task_index:
                    stdscr.addstr("".join([" ", task.name[:column - 2], " "]), curses.A_REVERSE)
                else:
                    stdscr.addstr(" ")
                    stdscr.addstr(task.name[:column - 2])
                offset_y += 1
                stdscr.move(offset_y, offset_x)
            offset_y = 6
            offset_x += column + 1

def print_project_info(stdscr, project):
    """
    Prints the project info.
    """
    stdscr.addstr(1, 1, project.name)
    for index, board in enumerate(project.boards):
        if index == project.active_board:
            stdscr.addstr(index + 3, 2, "".join(["* ", str(project.boards[index])]))
        else:
            stdscr.addstr(index + 3, 2, "".join(["  ", str(project.boards[index])]))

def print_board_info(stdscr, project):
    """
    Prints the board info.
    """
    stdscr.addstr(1, 1, "Board name:", curses.A_UNDERLINE)
    stdscr.addstr("".join([" ", project.get_active().name]))
    stdscr.addstr(3, 1, "Board description:", curses.A_UNDERLINE)
    stdscr.addstr("".join([" ", project.get_active().description]))
    stdscr.addstr(5, 1, "Board columns:", curses.A_UNDERLINE)
    for index, column in enumerate(project.get_active().columns):
        stdscr.addstr(index + 6, 1, str(column.name))

def print_column_info(stdscr, project, selection):
    """
    Prints the column info.
    """
    stdscr.addstr(1, 1, "Column name:", curses.A_UNDERLINE)
    stdscr.addstr("".join([" ", project.get_active().columns[selection[1]].name]))
    stdscr.addstr(3, 1, "Column description:", curses.A_UNDERLINE)
    stdscr.addstr("".join([" ", project.get_active().columns[selection[1]].description]))
    stdscr.addstr(5, 1, "Column task limit:", curses.A_UNDERLINE)
    stdscr.addstr("".join([" ", str(project.get_active().columns[selection[1]].task_limit)]))

def print_box(stdscr, y, x, print_string, attribute=None):
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
    if attribute is None:
        stdscr.addstr(y + 1, 1, "".join([" ", print_string, " "]))
    else:
        stdscr.addstr(y + 1, 1, "".join([" ", print_string, " "]), attribute)
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
        # If there is a split, split at the closing parenthesis as well.
        if item.count("(") == item.count(")") == 1:
            split_text = item.split("(")
            if len(split_text) > 1:
                split_text[1] = split_text[1].split(")")
            # If the first part is longer than 0, print it in normal text.
            if len(split_text[0]) > 0:
                stdscr.addstr(max_yx[0] - 1, 1 + offset, split_text[0])
            # Print the underlined part.
            stdscr.addstr(max_yx[0] - 1, 1 + offset + len(split_text[0]), split_text[1][0], curses.A_UNDERLINE)
            if len(split_text[1][1]) > 0:
                stdscr.addstr(max_yx[0] - 1, 1 + offset + len(split_text[0]) + len(split_text[1][0]), split_text[1][1])
        else:
            stdscr.addstr(max_yx[0] - 1, 1 + offset, item)
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

def remove_board(stdscr, project):
    """
    Lets the user select a board and removes it.
    """

    selection = 0

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
    project.boards.pop(selection)

if __name__ == "__main__":
    curses.wrapper(main)
    
