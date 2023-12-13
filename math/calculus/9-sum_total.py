#!/usr/bin/env python3

"""summation of i squared"""


def summation_i_squared(n):
    """
    Function to sum of n squared:

    @param n - number of integers to calculate
    @return sum of n squared
    """

    if n < 1 or not isinstance(n, int):
        return None
    return sum(map(lambda n: n**2, range(n + 1)))
