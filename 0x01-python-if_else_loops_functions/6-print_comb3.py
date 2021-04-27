#!/usr/bin/python3
for L in range(0, 9):
    for J in range(L + 1, 10):
        if L == 8:
            print("{}{}".format(L, J))
        else:
            print("{}{}".format(L, J), end=", ")
