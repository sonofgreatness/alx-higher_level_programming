#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for element in list:
            print('{:d}'.format(element), end=" " if element != list[-1] else "")
        print()
