#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for l in a_dictionary:
            if l == key:
                a_dictionary[l] = value
    return a_dictionary
