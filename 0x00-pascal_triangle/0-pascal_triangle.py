#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Dispalys a list of lists of integers representing the pascal's triangle of n

    Args:
        n (int): rows' number
    """
    if n <= 0:
        return []
    res = []

    for k in range(n):
        row = []
        # colunms in row is k + 1
        for l in range(k + 1):
            # cell is at [row, cell]
            row.append(combination(k, l))
        res.append(row)

    return res


def combination(n, r):
    """Displays the combination of a n and r (nCr)

    Args:
        n (int): objects' of total number
        r (int): chosen objects' number
    """
    denominator = factorial(n - r) * factorial(r)
    return int(factorial(n) / denominator)


def factorial(n):
    """Displays the factorial of a number

    Args:
        n (int): number
    """
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
