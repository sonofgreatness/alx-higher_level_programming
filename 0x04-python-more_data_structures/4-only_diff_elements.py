#!/usr/bin/python3
"""
a function that returns a set of all elements present in only one set

"""


def common_elements(set_1, set_2) -> set:
    returnList = []
    for element_ in set_1:
        for element_1 in set_2:
            if element_ == element_1:
                returnList.append(element_1)
    return set(returnList)


def only_diff_elements(set_1, set_2) -> set:
    returnList = []
    checker_set = common_elements(set_1, set_2)

    for element_ in set_1:
        if element_ not in checker_set:
            returnList.append(element_)

    for element_ in set_2:
        if element_ not in checker_set:
            returnList.append(element_)
    return set(returnList)
