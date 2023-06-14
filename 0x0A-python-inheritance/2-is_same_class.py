#!/usr/bin/python3
"""
Function 2-is_same_class container
"""


def is_same_class(obj, a_class):
    """
    Check if object is an instance of the specified class
        Args:
            obj: object
            a_class: class to confirm with the object
            Returns: True if object is an instance of the class
                     or False if not member of class
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
