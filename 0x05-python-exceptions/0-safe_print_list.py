#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return (x)
    except IndexError:
        for element in my_list:
            counter = counter + 1
            print("{}".format(element), end="")
        print("")
        return (counter)
