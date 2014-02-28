#!/bin/env python3

import pyban
import strings

def print_header(board, width=80):

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
    print(_get_header_divider(columns))

    print(_get_names_line(board, columns))

    print(_get_header_divider(columns))

    print("")
    print("\n" + str(columns))

def _get_names_line(board, columns):
    return_string = "|"

    for i in range(len(board.get_columns())):
        return_string += _get_column_header(board, columns, i)
        return_string += "|"

    return return_string

def _get_column_header(board, columns, index):

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

def _get_header_divider(columns):
    
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
   

if __name__ == "__main__":
    board_list = pyban.BoardList()
    board_list.load()

    while True:

        # Print prompt
        try:
            command = input("[" + board_list.get_active().get_name() + "] : ")
        except AttributeError:
            command = input("[---] : ")


        if command == "quit":
          break
        elif command == "version":
            print("\n" + strings.name + " v" + strings.version + "\n")
        elif command == "help":
            print(strings.help)
        elif command == "boards":
            for i in range(0, len(board_list.get_board_list())):
                print(str(i + 1) + ": " + str(board_list.get_board_list()[i]))
        elif command == "addboard":
            board_list.add_board()
            board_list.save()
        elif command == "use":
            try:
                board_list.set_active(int(input("Which board? ")) - 1)
            except IndexError:
                print("Invalid board number!")
            except ValueError:
                print("Board number must be an integer")
        elif command == "show":
            print_header(board_list.get_active())
        elif command == "name":
            if board_list.get_active() == None:
                print("Use the command \"use\" to make a board active first.")
            else:
                board_list.get_active().set_name(input("Enter new name: "))
                board_list.save()
