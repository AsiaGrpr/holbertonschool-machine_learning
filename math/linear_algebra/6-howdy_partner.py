#!/usr/bin/env python3

"""
Task 6 - "Howdy Partner"
objective: Concatenate arr
"""


def cat_arrays(arr1, arr2):
    """
    Function to concatenates two arrays
    """

    result = []

    len1 = len(arr1)
    for i in range(len1):
        result.append(arr1[i])

    for x in range(len(arr2)):
        result.append(arr2[x])

    return result
