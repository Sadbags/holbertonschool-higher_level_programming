#!/usr/bin/python3
""" Module that contains the Basegeometry class """


class BaseGeometry:
    """ Empty class """

    def area(self):
        """ raise exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
