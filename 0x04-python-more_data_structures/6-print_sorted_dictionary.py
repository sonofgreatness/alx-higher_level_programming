#!/usr/bin/python3
"""
Print dictionary by ordered keys

"""


def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())
    for element in sorted_dict:
        print("{}: {}".format(element[0], element[1]))
