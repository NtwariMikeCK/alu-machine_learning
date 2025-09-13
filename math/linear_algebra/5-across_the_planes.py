#!/usr/bin/env python3
"""
This module contains a function add_matrices2D that performs
element-wise addition of two 2D matrices.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First matrix
        mat2 (list of lists): Second matrix

    Returns:
        list of lists: New matrix containing element-wise sums
        None: If the matrices do not have the same shape
    """
    # Check if the number of rows is the same
    if len(mat1) != len(mat2):
        return None

    # Check if the number of columns in each row is the same
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None

    # Create a new matrix to store the result
    result = []

    # Loop through each pair of rows
    for row1, row2 in zip(mat1, mat2):
        new_row = []
        # Add elements of the rows element-wise
        for a, b in zip(row1, row2):
            new_row.append(a + b)
        result.append(new_row)

    return result
