#!/usr/bin/env python3
"""
This module contains a function matrix_transpose that returns
the transpose of a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): Input 2D matrix

    Returns:
        list of lists: Transposed matrix
    """
    transposed = []
    # Loop over columns of the original matrix
    for i in range(len(matrix[0])):
        new_row = []
        # Collect the i-th element from each row
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)

    return transposed
