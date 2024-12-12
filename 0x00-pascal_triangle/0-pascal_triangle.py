#!/usr/bin/python3
<<<<<<< HEAD
"""
0-pascal_triangle
=======
"""Pascal's triangle.
>>>>>>> 42181bc5f813e0ff28efa477d7ac58ed6fa0592c
"""


def pascal_triangle(n):
<<<<<<< HEAD
        """Return a list of lists of integers representing the pascal's triangle of n

            Args:
                    n (int): number of rows
                        """
                            if n <= 0:
                                        return []
                                        result = []

                                            for i in range(n):
                                                        row = []
                                                                # cols in row is i + 1
                                                                        for j in range(i + 1):
                                                                                        # cell is at [row, cell]
                                                                                                    row.append(combination(i, j))
                                                                                                            result.append(row)

                                                                                                                return result


                                                                                                            def combination(n, r):
                                                                                                                    """Return the combination of a n and r (nCr)

                                                                                                                        Args:
                                                                                                                                n (int): total number of objects
                                                                                                                                        r (int): number of chosen objects
                                                                                                                                            """
                                                                                                                                                denominator = factorial(n - r) * factorial(r)
                                                                                                                                                    return int(factorial(n) / denominator)


                                                                                                                                                def factorial(n):
                                                                                                                                                        """Return the factorial of a number

                                                                                                                                                            Args:
                                                                                                                                                                    n (int): number
                                                                                                                                                                        """
                                                                                                                                                                            if n < 2:
                                                                                                                                                                                        return 1
                                                                                                                                                                                        else:
                                                                                                                                                                                                    return n * factorial(n - 1)
=======
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
>>>>>>> 42181bc5f813e0ff28efa477d7ac58ed6fa0592c
