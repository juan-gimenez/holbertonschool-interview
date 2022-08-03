#!/usr/bin/python3
"""
lockboxes interview prep
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    lenb = len(boxes)
    list = [0]
    for i in list:
        for j in boxes[i]:
            if j not in list:
                if j < lenb:
                    list.append(j)
    if len(list) == lenb:
        return True
    return False
