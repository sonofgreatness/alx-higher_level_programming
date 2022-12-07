#!/usr/bin/python3
"""Prints the sum of all arguments"""
from sys import argv
if __name__ == "__main__": 
 def sum():
    sum = 0
    num_args = len(argv)
    if (num_args == 1):
        return sum
    else:
        for i in range(1, num_args):
            sum += int(argv[i])
    return sum


 print("{:d}".format(sum()))
