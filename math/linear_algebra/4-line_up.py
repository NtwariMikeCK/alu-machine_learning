#!/usr/bin/env python3
"""
This module contains a function add_arrays that performs
element-wise addition of two 1D arrays (lists).
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list of int/float): First array
        arr2 (list of int/float): Second array

    Returns:
        list: New array containing element-wise sums
        None: If the arrays do not have the same length
    """
    # Check if lengths match
    if len(arr1) != len(arr2):
        return None

    # Perform element-wise addition
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a + b)

    return result
