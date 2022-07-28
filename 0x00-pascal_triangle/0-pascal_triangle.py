#!/usr/bin/python3
"""
pascal_triangle(n)
"""


def pascal_triangle(n):
    """  list of lists of integers 
    representing the Pascal’s triangle of n
    return empty list if n is 0 or less
    """
    emplist = []
    if n <= 0:
        return emplist
    if n == 1:
        return [[1]]
    toap = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(toap[x-1][y-1] + toap[x-1][y])
        row.append(1)
        toap.append(row)
    return toap
