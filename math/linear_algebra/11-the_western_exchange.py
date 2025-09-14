#!/usr/bin/env python3
"""
This module contains a function np_transpose that returns
the transpose of a NumPy ndarray.
"""


def np_transpose(matrix):
    """
    Returns the transpose of a NumPy ndarray.

    Args:
        matrix (numpy.ndarray): Input array

    Returns:
        numpy.ndarray: Transposed array (new view of the data)
    """
    return matrix.T
