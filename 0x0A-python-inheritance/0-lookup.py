#!/usr/bin/python3
"""Module 0-lookup.
Find a list of available attributes of an object.
"""


def lookup(obj):
    """Returns that list of attributes.
    Args: - obj: object to look for
    """

    return dir(obj)
