#!/usr/bin/python3
""" a basic class """


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ initializes the students class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dict """
        if attrs is None:
            return self.__dict__

        Newdict = {}
        for a in attrs:
            try:
                Newdict[a] = self.__dict__[a]
            except KeyError:
                pass
            return Newdict

    def reload_from_json(self, json):
        """ replace all attr of student """
        for key in json:
            try:
                setattr(self, key, json[key])
            except KeyError:
                pass
