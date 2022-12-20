#!/usr/bin/python3

"""
function that divides element by element 2 lists

my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists

Returns a new list (length = list_length) with all divisions

If 2 elements can’t be divided, the division result should be equal to 0

If an element is not an integer or float:
print: wrong type

If the division can’t be done (/0):
print: division by 0

If my_list_1 or my_list_2 is too short
            print: out of range

You have to use try: / except: / finally:
"""


def list_division(my_list_1, my_list_2, list_length):
    returnList = []
    if (len(my_list_1) < list_length or len(my_list_2) < list_length):
        print("out of range")

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            break
        finally:
            returnList.append(result)
    return (returnList)
