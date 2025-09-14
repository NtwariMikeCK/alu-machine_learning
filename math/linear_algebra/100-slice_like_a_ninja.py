#!/usr/bin/env python3
"""
This module contains a function np_slice that slices
a NumPy ndarray along specific axes.
"""


def np_slice(matrix, axes={}):
    """
    Slices a NumPy ndarray along given axes.

    Args:
        matrix (numpy.ndarray): Input array
        axes (dict): Dictionary where the key is an axis index
                     and the value is a tuple specifying the slice

    Returns:
        numpy.ndarray: The sliced array
    """
    # Build slice objects for each axis
    slices = [slice(*axes.get(i, (None, None, None)))
              for i in range(matrix.ndim)]
    return matrix[tuple(slices)]
