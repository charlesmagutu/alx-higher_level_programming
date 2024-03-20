#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    transpose = []
    for x in range(3):
        transpose.append([row[x] for row in matrix])
    return transpose
