#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for row in transposed:
        print(" ".join(map(str, row)))
