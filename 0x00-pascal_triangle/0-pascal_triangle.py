#!/usr/bin/python3
"""Pascal's triangle.
"""


def pascal_triangle(n):
    """Displays a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for k in range(n):
        line = []
        for l in range(k + 1):
            if l == 0 or l == k:
                line.append(1)
            elif k > 0 and l > 0:
                line.append(triangle[k - 1][l - 1] + triangle[k - 1][l])
        triangle.append(line)
    return triangle
