#!/usr/bin/env python3

"""
Task 7 - "Gettin’ Cozy"
objective: Concatenate matrices
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Function to concatenates two matrices along a specific axis
    """

    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return mat1 + mat2
    elif axis != 0 and len(mat1) == len(mat2):
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
