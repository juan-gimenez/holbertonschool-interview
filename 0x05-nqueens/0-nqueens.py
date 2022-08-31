#!/usr/bin/python3
"""N Queens Problem"""
import sys as s


def cons(a, N: int):
    """"""
    tmp = []
    for i in range(N):
        for j in range(N):
            for k, l in a:
                if i == k or j == l or abs((j - l)/(k - i)) == 1:
                    break
            else:
                tmp.append([i, j])

    return tmp


def check(a, tmp, col: int, N: int):
    """i"""
    if len(a) == N or len(tmp) < len(a):
        return a
    if len(a) == 0:
        a.append([0, col])
    # if len(tmp) == 0:
    tmp = cons(a, N)
    next_candidate = tmp[0]
    if next_candidate in tmp:
        a.append(next_candidate)
        return check(a, tmp, col, N)


if __name__ == '__main__':
    if len(s.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    if not s.argv[1].isdigit():
        print('N must be a number')
        exit(1)

    N = int(s.argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)

    for i in range(N):
        solution = check([], [], i, N)
        if len(solution) == N:
            print(solution)
