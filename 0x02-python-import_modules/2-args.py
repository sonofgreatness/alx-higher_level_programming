#!/usr/bin/python3
"""Prints arguments of
    a program
"""
from sys import argv
if __name__ == '__main__':
    num_args = len(argv)
    if (num_args == 1):
        print("{} arguments.".format(0))
    elif (num_args == 2):
        print("{} argument:".format(num_args - 1))
        print("{}: {}".format(num_args - 1, argv[num_args - 1]))
    else:
        print("{} arguments:".format(num_args - 1))
        for i in range(1, num_args):
            print("{}: {}".format(i, argv[i]))
