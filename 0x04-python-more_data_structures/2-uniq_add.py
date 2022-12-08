#!/usr/bin/python3
"""

function that adds all unique integers in a list (only once for each integer).

"""


def uniq_add(my_list=[]):
    sum = 0
    list_set = set(my_list)
    for element in list_set:
        sum = sum + int(element)
    return sum
