# -*- coding: utf-8 -*-
import json, yaml

def uni_parse(file_to_parse):
    """Parser functions"""
    if file_to_parse.suffix == '.json':
        with open(file_to_parse):
            parsed_file = json.load(file_to_parse)
    else:
        with open(file_to_parse):
            parsed_file = yaml.safe_load(file_to_parse)

    return parsed_file
