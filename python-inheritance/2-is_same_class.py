#!/usr/bin/python3
""" module that contains a class """


def is_same_class(obj, a_class):
    """ Return True is obj isinstance """

    if type(obj) == a_class:
        return True

    else:
        return False
