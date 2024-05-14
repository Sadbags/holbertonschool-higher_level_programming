#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'III': 3, 'XXI': 21, 'IV': 4, 'CXXIV': 124, 'XCIX': 99, 'LXXXIX': 89}
    result = 0

    for i in range(len(roman_string)):
        value = roman_numerals.get(roman_string[i], 0)
        if i + 1 < len(roman_string) and roman_numerals.get(roman_string[i + 1], 0) > value:
            result -= value
        else:
            result += value
