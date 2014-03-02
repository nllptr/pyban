#!/bin/env python3

import pyban
import strings

def _print_header(board, width=80):

    column = (width - 1) // len(board.get_columns())
    remains = (width - 1) % len(board.get_columns())
    columns = []

    # Create columns list (spread evenly, remaining to the left)
    for i in range(0, len(board.get_columns())):
        columns.append(column)
        if remains > 0:
            columns[i] += 1
            remains -= 1

    print("")
    print(__get_header_divider(columns))

    print(__get_names_line(board, columns))

    print(__get_header_divider(columns))

    # Get the length of the biggest task list.
    max_tasks = 0
    for col in board.get_columns():
        if len(col.get_tasks()) > max_tasks:
            max_tasks = len(col.get_tasks())

    for i in range(max_tasks):
        print("|", end="")
        for column_index in range(len(board.get_columns())):
            if len(board.get_column(column_index).get_tasks()) <= i:
                __print_task(column_index, columns[column_index])
            else:
                __print_task(column_index, columns[column_index], board.get_column(column_index).get_tasks()[i])
            print("|", end="")
        print("\n", end="")

    print(__get_header_divider(columns))

    print("")
    print("\n" + str(columns))
    for cols in board.get_columns():
        for tasks in cols.get_tasks():
            print(tasks.get_name())

    print(max_tasks)

def __print_task(column_index, column_width, task=None):
    if task == None:
        print(" " * (column_width - 1), end="")
    else:
        return_string = " "
        column_width -= 1
        if len(task.get_name()) < column_width:
            for c in task.get_name():
                return_string += c
                column_width -= 1
            return_string += (" " * (column_width - 1))
        else:
            return_string += task.get_name()[:column_width - 1]
        print(return_string, end="")

def __get_names_line(board, columns):
    return_string = "|"

    for i in range(len(board.get_columns())):
        return_string += ___get_column_header(board, columns, i)
        return_string += "|"

    return return_string

def ___get_column_header(board, columns, index):

    # Compensate for one empty space at each end of the string
    string_width = columns[index] - 2
    letters_width = len(board.get_column(index).get_name())
    return_string = " "

    if letters_width > string_width:
        for i in range(string_width):
            return_string += board.get_column(index).get_name()[i]
    else:
        for i in range(string_width):
            if i < letters_width:
                return_string += board.get_column(index).get_name()[i]
            else:
                return_string += " "

    return return_string

def __get_header_divider(columns):
    
    return_string = ""

    # Print first divider
    return_string += "+"

    # Print columns
    for i in columns:

        # Compensate for divider character.
        i -= 1
        for j in range(i):
            return_string += "-"
        return_string += "+"

    return return_string

def _print_board_list():
    for i in range(0, len(board_list.get_board_list())):
        print(str(i + 1) + ": " + str(board_list.get_board_list()[i]))
  

if __name__ == "__main__":
    board_list = pyban.BoardList()
    board_list.load()

    while True:

        # Print prompt
        try:
            new_input = input("[" + board_list.get_active().get_name() + "]: ").split()
        except AttributeError:
            new_input = input("[ --- ]: ").split()

        command = new_input[0]
        parameters = new_input[1:]

        # QUIT
        if command == "quit":
          break

        # VERSION
        elif command == "version":
            print("\n" + strings.name + " v" + strings.version + "\n")

        # HELP
        elif command == "help":
            print(strings.full_help)

        # USE
        elif command == "use":
            if len(parameters) == 0:
                _print_board_list()
            else:
                try:
                    board_list.set_active(int(parameters[0]) - 1)
                except IndexError:
                    print("Format: " + strings.format_use)
                except ValueError:
                    print("Format: " + strings.format_use)

        # ADD
        elif command == "add":
            if len(parameters) == 0:
                print("Format: " + strings.format_add)
            elif parameters[0] == "board":
                # Create board
                if len(parameters[1:]) == 0:
                    board_list.add_board()
                else:
                    board_list.add_board(" ".join(parameters[1:]))
            elif parameters[0] == "col":
                # Create column in active board
                if len(parameters[1:]) == 0:
                    print("Format: " + strings.format_add)
                elif len(parameters[1:]) == 1:
                    board_list.get_active().add_column(int(parameters[1]) - 1)
                else:
                    board_list.get_active().add_column(int(parameters[1]) - 1, parameters[2:])
            elif parameters[0] == "task":
                # Create task in active board
                try:
                    if len(parameters) == 1:
                        board_list.get_active().get_column(0).add_task()
                    if len(parameters) >= 2:
                        board_list.get_active().get_column(0).add_task(" ".join(parameters[1:]))
                except IndexError:
                    print("No columns!")

        # DEL
        elif command == "del":
            if len(parameters) != 2:
                print("Format: " + strings.format_del)
            elif parameters[0] == "board":
                # Delete board
                try:
                    print("Delete board " + str(board_list.get_board(int(parameters[1]) - 1)) + "?")
                    if input("y/N: ") == "y":
                        board_list.remove_board(int(parameters[1]) - 1)
                except IndexError:
                    print("Format: " + strings.format_del_board)

            elif parameters[0] == "col":
                # Delete column
                try:
                    print("Delete column " + board_list.get_active().get_column(int(parameters[1]) - 1).get_name() + "?")
                    if input("y/N: ") == "y":
                        board_list.get_active().remove_column(int(parameters[1]) - 1)
                except IndexError:
                    print("Format: " + strings.format_del_col)
            elif parameters[0] == "task":
                # Delete task
                pass

        # SHOW
        elif command == "show":
            _print_header(board_list.get_active())

        # BOARD
        elif command == "board":
            # !!!! this might change (get would only have 2 params)
            if len(parameters) < 3:
                print("Format: " + strings.format_board)
            else:
                if parameters[0] == "set":
                    if parameters[1] == "name":
                        board_list.get_active().set_name(" ".join(parameters[2:]))
                    elif parameters[1] == "desc":
                        board_list.get_active().set_description(" ".join(parameters[2:]))
                    else:
                        print("Format: " + strings.format_board)
                else:
                    print("Format: " + strings.format_board)

        # COL
        elif command == "col":
            # !!!! Might change if get options are introduced.
            if len(parameters) < 4:
                print("Format: " + strings.format_col)
            elif parameters[0] == "set":
                if parameters[1] == "name":
                    try:
                        board_list.get_active().get_column(int(parameters[2]) - 1).set_name(" ".join(parameters[3:]))
                    except IndexError:
                        print("Format: " + strings.format_col_set_name)
                    except ValueError:
                        print("Format: " + strings.format_col_set_name)
                elif parameters[1] == "desc":
                    try:
                        board_list.get_active().get_column(int(parameters[2]) - 1).set_description(" ".join(parameters[3:]))
                    except IndexError:
                        print("Format: " + strings.format_col_set_desc)
                elif parameters[1] == "sub":
                    #set sub board
                    pass
                else:
                    #show error
                    pass
                
        # INVALID INPUT
        else:
            print(strings.unknown_command)

        board_list.save()
