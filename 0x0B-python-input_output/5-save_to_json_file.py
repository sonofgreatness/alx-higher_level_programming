#!/usr/bin/python3
"""
save_to_json_file that  writes an Object to a
text file, using a JSON representation:

Args
    my_obj  - object to write
    filename (string) - name of file

"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
