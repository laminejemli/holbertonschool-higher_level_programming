#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[m ** 2 for m in row] for row in matrix]
