#!/usr/bin/python3
'''
calculates how many coins are
needed to achieve total
'''


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to
    meet a given amount total for given pile of coins
    """

    # total is 0 or less, return 0
    if total <= 0:
        return 0

    num = 0
    for coin in sorted(coins, reverse=True):
        if total == 0:
            return num
        num += total // coin
        total %= coin

    if total == 0:
        return num
    # total cannot be met by any number of coins you have
    return -1
