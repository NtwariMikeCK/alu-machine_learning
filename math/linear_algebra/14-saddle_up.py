#!/usr/bin/env python3
"""
This module contains a function np_matmul that performs
matrix multiplication using NumPy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication on two NumPy arrays.

    Args:
        mat1 (numpy.ndarray): First matrix
        mat2 (numpy.ndarray): Second matrix

    Returns:
        numpy.ndarray: Result of the matrix multiplication
    """
    return np.matmul(mat1, mat2)
