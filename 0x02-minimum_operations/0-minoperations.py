#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    """
    ret = 0
    tmp = 2

    if type(n) != int:
        return 0

    if type(n) == int and n < 2:
        return 0

    while tmp <= n + 1:
        if n % tmp == 0:
            ret += tmp
            n //= tmp
            tmp = 2
        else:
            tmp += 1

    return ret
