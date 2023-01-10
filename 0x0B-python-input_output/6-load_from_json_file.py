#!/usr/bin/python3
"""
creates an Object from a “JSON file”
 Args
    filename (string) name of file

 ReTursn:
     object

"""

import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        return (json.load(f))
