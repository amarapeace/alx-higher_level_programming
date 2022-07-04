#!/usr/bin/python3

def no_c(my_string):
    new_string = ""

    for letter in range(len(my_string)):
        if (letter != "c") and (letter != "C"):
            new_string += letter
        return new_string
