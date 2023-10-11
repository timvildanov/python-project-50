import json


def json_format(diff):
    return json.dumps(diff, indent=4, sork_keys=True)
