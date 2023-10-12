from pathlib import Path
from gendiff.file_parser import uni_parse
from gendiff.formats.json import json_format
from gendiff.formats.plain import plain
from gendiff.formats.string import string

FORMATTER = {'string': string,
             'plain': plain,
             'json': json_format()}
def build_diff(initial_dict, changed_dict):
    """Function creates a difference between two dictionaries"""
    diff_dict = {}
    pass

def generate_diff(first_file, second_file, format = 'string'):
    try:
        first_file = uni_parse(Path(first_file))
        second_file = uni_parse(Path(second_file))
        parse_file = [first_file, second_file]
    except FileNotFoundError:
        return print('Wrong path')

    return FORMATTER[format](build_diff(parse_file))