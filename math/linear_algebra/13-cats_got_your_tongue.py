#!/usr/bin/env python3

"""
Task 13 - "Cat's Got Your Tongue"
objective: Concatenate matrices
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Function to concatenates two matrices along a specific axis with numpy
    """

    return np.concatenate((mat1, mat2), axis)
