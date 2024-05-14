#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

a_dictionary = {'a': 1, 'b': 2, 'c': 3}
key_to_delete = 'b'
print(simple_delete(a_dictionary, key_to_delete))
