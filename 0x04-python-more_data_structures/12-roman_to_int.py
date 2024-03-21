#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    total = 0
    prev_val = 0

    for char in reversed(roman_string):
        val = dict_roman.get(char)
        if val is None:
            return 0

        if val >= prev_val:
            total += val
        else:
            total -= val
        prev_val = val
    return total
