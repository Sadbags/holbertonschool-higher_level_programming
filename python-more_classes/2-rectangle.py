#!/usr/bin/python3
""" Module contain class rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """
    __width = None
    __height = None

    def __innit__(self, width=0, height=0):
        """ Defines a rectangle class width and height """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Initializes height and width for rectangle class """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        def area(self):
            return self.__width * self.__height

        def perimeter(self):

            if self.__width == 0 or self.__height == 0:
                return 0
            return (self.__width * 2) + (self.height * 2)
