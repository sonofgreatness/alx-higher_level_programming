#!/usr/bin/python3

"""
writes to a files
    Args:
      filesname (string) name of file
      text (string) text to write file

    Returns:
        nummber of characters written to file

"""


def write_file(filename="", text=""):
    counter = 0
    with open(filename, 'w', encoding="UTF-8") as f:
        return (f.write(text))
