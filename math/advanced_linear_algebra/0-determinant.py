#!/usr/bin/env python3

"""
  Calculates the determinant of a matrix.
  Args:
   matrix: list of lists representing a square matrix
    Returns:
        The determinant value (int or float)
    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.
    Args:
        matrix: list of lists representing a square matrix
    Returns:
        The determinant value (int or float)
    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not square
    """

    # --- Type checks ---
    if type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # --- Handle empty input [] separately ---
    if matrix == []:
        raise ValueError("matrix must be a square matrix")

    rows = len(matrix)
    # --- Handle 0x0 matrix ---
    if matrix == [[]]:
        return 1

    # --- Check square ---
    if not all(len(row) == rows for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # --- Base cases ---
    if rows == 1:
        return matrix[0][0]
    if rows == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # --- Recursive Laplace expansion (first row) ---
    det = 0
    for col in range(rows):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det
