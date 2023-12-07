#!/usr/bin/env python3

"""
Task 12 - "Bracing The Elements"
objective: Make element-wise operations in matrix
"""


def np_elementwise(mat1, mat2):
    """
    Function to make element-wise operations on matrices with numpy
    """

    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2

    return add, sub, mul, div
