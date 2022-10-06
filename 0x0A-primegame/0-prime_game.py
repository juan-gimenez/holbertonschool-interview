#!/usr/bin/python3
"""
solution to the Prime Game problem
"""


def primes(n):
    """ return prime numb
    """
    prime = []
    pri = [True] * (n + 1)
    for p in range(2, n + 1):
        if (pri[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                pri[i] = False
    return prime

            
def isWinner(x, nums):
    """
    sets winner or none
    """
    if x is None or nums is None:
        return None
    if x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben = Ben + 1
        else:
            Maria = Maria + 1
    if Ben > Maria:
    # ben win
        return 'Ben'
    elif Maria > Ben:
    # maria win
        return 'Maria'
    return None
