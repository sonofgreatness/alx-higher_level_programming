#!/usr/bin/python3
"""
read file 
Args : 
    filename (string)   name o file to open 
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="UTF-8") as f:
            print(f.read())
