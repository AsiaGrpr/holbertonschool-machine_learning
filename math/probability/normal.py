#!/usr/bin/env python3
"""
Task 6 - Initialize Normal
"""


class Normal:
    """
    Normal class that represents a normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))
            self.stddev = float(
                (sum((x - self.mean)**2 for x in data) / len(data)) ** 0.5)

    def z_score(self, x):
        """
        Function to calculate the z-score of a given x-value
        """

        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Function to calculate the x-score given z-score
        """

        return self.mean + z * self.stddev
