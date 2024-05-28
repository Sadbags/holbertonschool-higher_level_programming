#!/usr/bin/python3
""" write a string to text file and returns number of chars written """


def write_file(filename="", text=""):
    """ writing file """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
