#!/usr/bin/env python3

"""
Task 4 - "Line Up"
objective: Make element-wise operations in arr
"""


def add_arrays(arr1, arr2):
    """
    Function to adds two arrays element-wise
    """

    results = []
    lenght1 = len(arr1)
    lenght2 = len(arr2)

    if lenght1 != lenght2:
        return None

    for i in range(lenght1):
        results.append(arr1[i] + arr2[i])
    return results
