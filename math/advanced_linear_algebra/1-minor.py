#!/usr/bin/env python3
"""
dule to calculate the minor matrix of a square matrix
"""


def minor(matrix):
    """
    Calculates the minor matrix of a square matrix

    Args:
        matrix: list of lists representing a square matrix

    Returns:
        list of lists representing the minor matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square or is empty
    """
    if (type(matrix) is not list or
            not all(type(row) is list for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if n == 0 or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minors = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:]
                         for k, row in enumerate(matrix) if k != i]
            minor_row.append(determinant(submatrix))
        minors.append(minor_row)

    return minors
