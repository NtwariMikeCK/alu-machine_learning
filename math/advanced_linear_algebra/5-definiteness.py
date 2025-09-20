#!/usr/bin/env python3
"""
Module to calculate the definiteness of a matrix
"""

import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a square matrix

    Args:
        matrix (np.ndarray): matrix to classify

    Returns:
        str: "Positive definite", "Positive semi-definite",
             "Negative definite", "Negative semi-definite",
             "Indefinite", or None if not applicable

    Raises:
        TypeError: if matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2:
        return None
    n, m = matrix.shape
    if n != m or n == 0:
        return None

    # Ensure matrix is symmetric (only symmetric matrices have definiteness)
    if not np.allclose(matrix, matrix.T):
        return None

    # Compute eigenvalues
    eigvals = np.linalg.eigvals(matrix).real

    if np.all(eigvals > 0):
        return "Positive definite"
    if np.all(eigvals >= 0):
        return "Positive semi-definite"
    if np.all(eigvals < 0):
        return "Negative definite"
    if np.all(eigvals <= 0):
        return "Negative semi-definite"
    if np.any(eigvals > 0) and np.any(eigvals < 0):
        return "Indefinite"

    return None
