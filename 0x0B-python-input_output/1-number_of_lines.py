#!/usr/bin/python3
"""
Contains the number_of_lines function
"""


def write_file(filename="", text=""):
    """uses open() and write() to write string to a text file.
    Return:
        no of characters read
    Args:
        filename: text file to write into
        text (str): string to write to text file
    """
    with open(filename, 'w', encoding='utf8') as file:
        return file.write(text)
