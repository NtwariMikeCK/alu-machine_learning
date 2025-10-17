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
        self.d = d  # store number of dimensions
    
    def pdf(self, x):
        """
        Calculates the PDF at a given data point x.
        Parameters:
        x (numpy.ndarray): A numpy array of shape (d, 1) containing the data point
        Returns:
        float: The PDF value at x
        Raises:
        TypeError: If x is not a numpy.ndarray
        ValueError: If x doesn't have the correct shape
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if x.shape != (self.d, 1):
            raise ValueError(f"x must have the shape ({self.d}, 1)")
        # Center x
        diff = x - self.mean
        # Determinant and inverse of covariance matrix
        det_cov = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        # Multivariate normal PDF formula:
        # PDF(x) = (1 / sqrt((2π)^d * |Σ|)) * exp(-0.5 * (x-μ)ᵀ * Σ^(-1) * (x-μ))
        norm_const = 1 / (np.sqrt((2 * np.pi) ** self.d * det_cov))
        exponent = -0.5 * (diff.T @ inv_cov @ diff)
        return float(norm_const * np.exp(exponent))
