#!/usr/bin/env python3

"""
Task 2 - "Size me please" 
objective: Find matric shape
"""


def matrix_shape(matrix):
    """
    Function to calculate the shape of a matrix using
    isinstance function in case there is nested list
    """

    shape = []
    while isinstance(matrix, list):
        if not matrix:
            return shape
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
