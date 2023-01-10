#!/usr/bin/python3
"""
returns an object (Python data structure)

"""


import json


def from_json_string(my_str):
    with open('file_X.txt', 'w', encoding="UTF-8") as f:
        f.write(my_str)
        f.close()
    with open('file_X.txt', 'r', encoding="UTF-8") as f:
        return (json.load(f))
