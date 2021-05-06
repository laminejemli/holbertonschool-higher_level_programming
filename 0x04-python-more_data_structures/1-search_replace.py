#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = []
    for l in range(len(my_list)):
        if my_list[l] == search:
            cpy.append(replace)
        else:
            cpy.append(my_list[l])
    return cpy
