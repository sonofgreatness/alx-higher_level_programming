#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    returnList = []
    for list_ in matrix:
        new_list = list(map(lambda x: x**2, list_))
        returnList.append(new_list)
    return returnList
