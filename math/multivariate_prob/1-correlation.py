#!/usr/bin/env python3
"""correlation class"""
import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix.
    Parameters:
    C (numpy.ndarray): A 2D square numpy array of shape (d, d)
      containing the covariance matrix.
    Returns:
    numpy.ndarray: A 2D numpy array of shape (d, d) containing
      the correlation matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    # Standard deviations along the diagonal
    std_dev = np.sqrt(np.diag(C))
    # Outer product of standard deviations
    denom = np.outer(std_dev, std_dev)
    # Correlation matrix
    corr_matrix = C / denom
    # Fill diagonal with 1.0 to avoid any floating-point issues
    np.fill_diagonal(corr_matrix, 1.0)
    return corr_matrix
