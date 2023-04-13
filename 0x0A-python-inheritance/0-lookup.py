#!/usr/bin/python3
"""
Defines an object attribute lookup function.
"""


def lookup(obj):
    """Return object available attributes list."""
    return (dir(obj))
