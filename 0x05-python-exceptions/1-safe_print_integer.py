#!/usr/bin/python3

"""
safe_print_integer - prints an integer
if @param is not an integer throws and
exception
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value + 0))
        return (True)
    except TypeError:
        return (False)
