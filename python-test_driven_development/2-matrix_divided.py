#!/usr/bin/python3
"""

Function that devides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
Function that devides all elements of a matrix
"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for j in i:
        if type(j) is not int and type(j) is not float:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
