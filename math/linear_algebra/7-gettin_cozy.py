#!/usr/bin/env python3
"""
7-gettin_cozy.py

This module contains a function cat_matrices2D that concatenates
two 2D matrices along a specified axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along the given axis.

    Args:
        mat1 (list of lists): First matrix
        mat2 (list of lists): Second matrix
        axis (int): 0 to concatenate rows, 1 to concatenate columns

    Returns:
        list of lists: New concatenated matrix
        None: If the matrices cannot be concatenated or axis is invalid
    """
    # Axis 0: concatenate rows
    if axis == 0:
        # Check that number of columns matches
        cols1 = len(mat1[0]) if mat1 else 0
        cols2 = len(mat2[0]) if mat2 else 0
        if cols1 != cols2:
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Axis 1: concatenate columns
    elif axis == 1:
        # Check that number of rows matches
        if len(mat1) != len(mat2):
            return None
        new_matrix = []
        for row1, row2 in zip(mat1, mat2):
            new_matrix.append(row1[:] + row2[:])
        return new_matrix

    # Invalid axis
    else:
        return None
