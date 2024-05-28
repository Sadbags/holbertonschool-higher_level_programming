#!/usr/bin/python3
""" append a string at end of text file  """


def write_file(filename="", text=""):
    """ append a string """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
