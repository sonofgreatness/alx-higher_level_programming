#!/usr/bin/python3

"""
adds all arguments to a Python list, and then save them to a file

  Takes arguments


"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_args = sys.argv[1:]
save_to_json_file(my_args, filename)
load_from_json_file(filename)
