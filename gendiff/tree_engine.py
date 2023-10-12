from pathlib import Path
from gendiff.file_parser import uni_parse
from gendiff.formats.json import json_format
from gendiff.formats.plain import plain
from gendiff.formats.string import string

FORMATTER = {'string': string,
             'plain': plain,
             'json': json_format}

def build_diff(initial_dict, changed_dict):
    """Function creates a difference between two dictionaries"""
    keys = initial_dict.keys() | changed_dict.keys()
    diff_dict = {}

    for key in keys:
        if all(map(lambda el: isinstance(el.get(key), dict), initial_dict, changed_dict)):
            diff_dict[key] = ['nested', build_diff([initial_dict[key], changed_dict[key]])]
        elif initial_dict.get(key) == changed_dict.get(key):
            diff_dict[key] = ['same', initial_dict.get(key)]
        elif key not in initial_dict:
            diff_dict[key] = ['added', changed_dict.get(key)]
        elif key not in changed_dict:
            diff_dict[key] = ['deleted', initial_dict.get(key)]
        else:
            diff_dict[key] = ['modified', initial_dict.get(key), changed_dict.get(key)]

    return diff_dict


def generate_diff(first_file, second_file, format='string'):
    try:
        first_file = uni_parse(Path(first_file))
        second_file = uni_parse(Path(second_file))
        parse_file = [first_file, second_file]
    except FileNotFoundError:
        return print('Wrong path')

    return FORMATTER[format](build_diff(parse_file))
