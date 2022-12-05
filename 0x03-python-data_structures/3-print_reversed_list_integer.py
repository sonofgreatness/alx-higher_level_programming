#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print("{element}".format(element=my_list[-1*(x + 1)]))
