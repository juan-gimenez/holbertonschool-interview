#!/usr/bin/python3
"""perimeter
"""


def island_perimeter(grid):
    """perimeter of an island, grid
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                p = p + 4
                # check if is not border
                if i > 0:
                    p = p - grid[i - 1][j]
                if i < len(grid) - 1:
                    p = p - grid[i + 1][j]
                if j > 0:
                    p = p - grid[i][j - 1]
                if j < len(grid) - 1:
                    p = p - grid[i][j + 1]
    return p
