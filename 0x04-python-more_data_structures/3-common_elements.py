#!/usr/bin/python3
"""
nction that returns
a set of common elements in two sets.

"""


def common_elements(set_1, set_2) -> set:
    returnList = []
    for element_ in set_1:
        for element_1 in set_2:
           if element_ == element_1:
               returnList.append(element_1)
    return set(returnList)
