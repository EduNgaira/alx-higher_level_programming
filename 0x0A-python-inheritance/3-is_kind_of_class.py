#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object is inherited or class instance

    Args:
        obj (any): Object
        a_class (type): Class to match object to.
    Returns:
        True - if object is inherited/class instance.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
