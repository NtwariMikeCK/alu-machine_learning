#!/usr/bin/env python3
"""
This module defines a function cat_matrices
that concatenates two matrices along a given axis.
"""


def shape(matrix):
    """Return the shape of a nested list (matrix)."""
    if isinstance(matrix, list):
        return (len(matrix),) + shape(matrix[0])
    return ()


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices (nested lists) along a specific axis.

    Args:
        mat1 (list): First matrix
        mat2 (list): Second matrix
        axis (int): Axis to concatenate along

    Returns:
        list: New concatenated matrix
        None: If shapes are incompatible
    """
    sh1, sh2 = shape(mat1), shape(mat2)

    if len(sh1) != len(sh2):
        return None

    # All dimensions except the axis must match
    for i, (d1, d2) in enumerate(zip(sh1, sh2)):
        if i != axis and d1 != d2:
            return None

    if axis == 0:
        return mat1 + mat2

    # Recurse into sublists
    return [cat_matrices(a, b, axis=axis - 1) for a, b in zip(mat1, mat2)]
