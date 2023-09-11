#!/usr/bin/python3
"""is_kind_of_class module.
Contains a function that compares an object with an instance and class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.
    """
    return isinstance(obj, a_class)