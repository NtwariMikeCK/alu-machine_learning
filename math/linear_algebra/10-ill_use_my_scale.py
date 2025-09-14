#!/usr/bin/env python3
"""
This module contains a function np_shape that calculates
the shape of a NumPy ndarray.
"""

import numpy as np


def np_shape(matrix):
    """
    Returns the shape of a NumPy ndarray.

    Args:
        matrix (numpy.ndarray): Input array

    Returns:
        tuple of int: Shape of the array
    """
    return matrix.shape
