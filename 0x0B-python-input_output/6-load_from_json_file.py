#!/usr/bin/python3
""" load_from_json_file module """
import json


def load_from_json_file(filename):
    """
    creates an Object from JSON 
    """
    with open(filename, encoding="UTF8") as Myfile:
        return json.load(Myfile)filea 
