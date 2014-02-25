#!/bin/env python3

import pyban
import strings

while True:

    command = input("pyban: ")

    if command == "quit":
        break
    elif command == "help":
        print(strings.string_help)
    elif command == "boards":
        print("lists boards")
    
