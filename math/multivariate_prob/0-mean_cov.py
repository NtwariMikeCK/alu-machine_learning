#!/usr/bin/env python3
"""Binomial distribution class"""
import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a dataset.
    Parameters:
    X (numpy.ndarray): A 2D numpy array of shape (n, d) containing the dataset.
    Returns:
    mean (numpy.ndarray): np array of containing the mean of the dataset.
    cov (numpy.ndarray): np numpy array containing the covariance matrix.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    # Calculate the mean
    mean = np.mean(X, axis=0, keepdims=True)
    # Center the data
    X_centered = X - mean
    # Compute the covariance matrix
    cov = (X_centered.T @ X_centered) / (n - 1)
    return mean, cov

