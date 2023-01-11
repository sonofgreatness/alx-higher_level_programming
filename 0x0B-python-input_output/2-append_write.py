#!/usr/bin/python3
"""
append a string at the end of a text file
Args:
    filename (string) name of the file
    text (string) text to append to file

Return:
    ruturns number of characters appended
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF-8") as f:
        return (f.write(text))
