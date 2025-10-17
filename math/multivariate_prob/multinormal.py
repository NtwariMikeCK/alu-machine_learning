#!/usr/bin/env python3
"""Module for Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """
    def __init__(self, data):
        """
        Class constructor.
        Parameters:
        data (numpy.ndarray): A 2D numpy array of shape (d, n)
            containing the dataset.
                d is the number of dimensions
                n is the number of data points
        Raises:
        TypeError: If data is not a 2D numpy.ndarray
        ValueError: If data contains less than 2 data points
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        # Compute mean (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)
        # Center data
        data_centered = data - self.mean
        # Compute covariance matrix (d, d)
        # Cov = (1/(n-1)) * X_centered @ X_centered.T
        self.cov = (data_centered @ data_centered.T) / (n - 1)
