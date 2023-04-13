#!/usr/bin/python3
"""
Defines function which adds attributes to objects
"""


def add_attribute(obj, att, value):
    """If possible, adds new attribute to an object.

    Args:
        obj (any): Object to add.
        att (str): Attribute to add.
        value (any): Attribute value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
