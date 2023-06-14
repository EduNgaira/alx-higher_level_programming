#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks whether object is inherited or class instance.

    Args:
        obj (any): Object
        a_class (type): Class to match object.
    Returns:
        True _ when object is inherited/class instance
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
