#!/usr/bin/python3
def fizzbuzz():
    for l in range(1, 101):
        if l % 15 == 0:
            print("FizzBuzz", end=" ")
        elif l % 3 == 0:
            print("Fizz", end=" ")
        elif l % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(l, end=" ")
