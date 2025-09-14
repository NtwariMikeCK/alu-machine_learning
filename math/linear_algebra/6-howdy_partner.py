#!/usr/bin/env python3
"""
This module contains a function cat_arrays that concatenates
two 1D arrays (lists) into a new list.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two 1D arrays (lists).

    Args:
        arr1 (list): First array
        arr2 (list): Second array

    Returns:
        list: New array containing elements of arr1 followed by arr2
    """
    result = arr1 + arr2
    return result
