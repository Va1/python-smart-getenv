import os
from ast import literal_eval

__version__ = '1.2.0'


def getenv(name, **kwargs):
    """
    Retrieves environment variable by name and casts the value to desired type.
    If desired type is list or tuple - uses separator to split the value.
    """
    default_value = kwargs.get('default', None)
    list_separator = kwargs.get('separator', ',')
    desired_type = kwargs.get('type')
    if not desired_type and default_value is not None:
        desired_type = type(default_value)

    value = os.getenv(name, None)

    if value is None:
        if default_value is None:
            return None
        else:
            return default_value

    if desired_type is bool:
        if value.lower() in ['false', '0']:
            return False
        else:
            return bool(value)

    if desired_type in (list, tuple):
        value = value.split(list_separator)
        return desired_type(value)

    if desired_type is dict:
        return dict(literal_eval(value))

    return desired_type(value)
