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
    else:
        sm = 0
        for i in range(1, n+1):
            sm += (i ** 2)

        return sm
