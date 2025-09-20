#!/usr/bin/env python3
"""
Module to calculate the adjugate matrix of a square matrix
"""


def determinant(matrix):
    """
    Recursively calculates the determinant of a square matrix
    """
    if matrix == [[]]:
        return 1

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        submatrix = [row[:col] + row[col + 1:]
                     for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det


def minor(matrix):
    """
    Calculates the minor matrix of a square matrix
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


def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix
    """
    minors = minor(matrix)
    n = len(minors)

    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            cofactor_row.append(((-1) ** (i + j)) * minors[i][j])
        cofactors.append(cofactor_row)

    return cofactors


def adjugate(matrix):
    """
    Calculates the adjugate matrix of a square matrix

    Args:
        matrix: list of lists representing a square matrix

    Returns:
        list of lists representing the adjugate matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square or is empty
    """
    cof = cofactor(matrix)
    # Transpose of the cofactor matrix
    return [list(row) for row in zip(*cof)]
