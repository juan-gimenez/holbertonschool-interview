#!/usr/bin/python3
""" validUTF8  """


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    def func(digit):
        """ checks digit """
        c = 0
        for i in range(7, -1, -1):
            if digit & (1 << i):
                c += 1
            else:
                break
        return c

    c = 0
    for j in data:
        if not c:
            c = func(j)
            if c == 0:
                continue
            if c == 1 or c > 4:
                return False
            c -= 1
        else:
            c -= 1
            if func(j) != 1:
                return False
    return c == 0
