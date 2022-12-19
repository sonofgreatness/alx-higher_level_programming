#!/usr/bin/python3
"""
 function that prints the first x elements of a list
 and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter = counter + 1
        except IndexError:
            raise IndexError('list index out of range')
            exit()
        except (ValueError, TypeError):
            pass
    print()
    return counter
