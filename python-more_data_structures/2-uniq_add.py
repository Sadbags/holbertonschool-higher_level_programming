#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set()
    for element in my_list:
        if isinstance(element, int):
            unique_integers.add(element)
    total = sum(unique_integers)
    return total
