#!/usr/bin/python3
"""

Fucntion that prints name

"""


def say_my_name(first_name, last_name=""):
    """

    Class say_my_name

    """

    error1 = "first_name must be a string"
    error2 = "lats_name must be a string"
    if type(first_name) is not str:
        raise TypeError(error1)
    if type(last_name) is not str:
        raise TypeError(error2)
    print("My name is {:s} {:s}".format(first_name, last_name))
