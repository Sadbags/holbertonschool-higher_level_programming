#!/usr/bin/python3
""" module of a class """


class BaseGeometry:
    """ raise exception """

    def area(self):
        """ raise exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
