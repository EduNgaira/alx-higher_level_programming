#!/usr/bin/python3
"""
Define lookup attribute function.
"""


def lookup(obj):
	"""
	Arguments:
	obj: object
	Returns: list of variables(attributes) and functions
	"""
    return (dir(obj))
