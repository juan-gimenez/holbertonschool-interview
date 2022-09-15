#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """ rotates a 2d matrix"""

    lenmatrix = len(matrix)
    for i in range(lenmatrix):
        for j in range(i, lenmatrix):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    x = len(matrix)
    for i in range(x // 2):
        for j in range(x):
            matrix[j][i], matrix[j][x - 1 -
                                    i] = matrix[j][x - 1 - i], matrix[j][i]
