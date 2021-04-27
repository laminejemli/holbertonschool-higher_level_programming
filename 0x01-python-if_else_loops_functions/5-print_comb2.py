#!/usr/bin/python3
for l in range(0, 100):
    if l == 99:
        print(l)
    else:
        print("{:0>2d}".format(l), end=", ")
