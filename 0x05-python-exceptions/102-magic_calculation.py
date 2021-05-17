#!/usr/bin/python3
def magic_calculation(a, b):
    sum = 0
    for l in range(1, 3):
        try:
            if l > a:
                raise Exception('Too far')
            else:
                sum += a ** b / l
        except:
            sum = b + a
            break
    return sum
