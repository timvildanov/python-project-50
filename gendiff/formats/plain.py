from gendiff.formats.string import get_bool_text

def value_view(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value in (True, False, None):
        return get_bool_text(value)
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def plain():
    pass