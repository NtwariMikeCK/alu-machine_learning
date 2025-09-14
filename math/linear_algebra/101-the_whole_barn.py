#!/usr/bin/env python3
"""
This module defines a function add_matrices
that adds two matrices of arbitrary depth.
"""


def add_matrices(mat1, mat2):
    """
    Adds two matrices element-wise.

    Args:
        mat1 (list): First matrix (list or nested list of ints/floats)
        mat2 (list): Second matrix (same shape as mat1)

    Returns:
        list: New matrix containing the sums
        None: If mat1 and mat2 are not the same shape
    """
    if type(mat1) != type(mat2):
        return None

    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return None
        result = []
        for a, b in zip(mat1, mat2):
            summed = add_matrices(a, b)
            if summed is None:
                return None
            result.append(summed)
        return result

    # base case: numbers
    return mat1 + mat2
