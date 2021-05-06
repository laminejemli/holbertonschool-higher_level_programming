#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for l in list(a_dictionary):
        if a_dictionary[l] == value:
            del a_dictionary[l]
    return a_dictionary
