#!/usr/bin/env python3
"""
This module contains a function matrix_shape that calculates
the shape (dimensions) of a nested list (matrix).
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix or nested list.

    Args:
        matrix (list): A nested list representing the matrix

    Returns:
        list of int: A list of integers representing the size
                     in each dimension
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
