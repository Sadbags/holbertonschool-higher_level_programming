#!/usr/bin/python3
""" Module that contains the BaseGeometry class """


class BaseGeometry:
    """ Empty class """

    def area(self):
        """ Raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
