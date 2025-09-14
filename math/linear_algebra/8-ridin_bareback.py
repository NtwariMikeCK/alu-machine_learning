#!/usr/bin/env python3
"""
8-ridin_bareback.py

This module contains a function mat_mul that performs
matrix multiplication on two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of two 2D matrices.

    Args:
        mat1 (list of lists): First matrix (m x n)
        mat2 (list of lists): Second matrix (n x p)

    Returns:
        list of lists: Resulting matrix (m x p)
        None: If the matrices cannot be multiplied
    """
    # Check if multiplication is possible
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix
    result = []

    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            # Compute dot product of row i from mat1 and column j from mat2
            total = 0
            for k in range(len(mat2)):
                total += mat1[i][k] * mat2[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
