#!/usr/bin/env python3

"""
Task 0 - Initialize Poisson
"""


class Poisson:
    """
    Poisson class that represents a poisson distribution
    """
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """
        Function to calculate the pmf for a given number
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        factorial_k = self.factorial(k)
        return (self.e ** (-self.lambtha) * self.lambtha ** k) / factorial_k

    def factorial(self, i):
        """
        Function to calculate the factorial of a number
        """
        if i < 0:
            return None
        if i == 0:
            return 1
        if i == 1:
            return 1
        return i * self.factorial(i - 1)

    def cdf(self, k):
        """
        Function to calculate the cdf for a given number
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum([self.pmf(x) for x in range(k + 1)])
