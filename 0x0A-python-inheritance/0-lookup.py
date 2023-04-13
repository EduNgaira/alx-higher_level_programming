#!/usr/bin/python3
"""
Defin lookup function.
"""


def lookup(obj):
	"""
	Args:
	obj: object
	Return: list of object's available attributes
	"""
    return (dir(obj))
