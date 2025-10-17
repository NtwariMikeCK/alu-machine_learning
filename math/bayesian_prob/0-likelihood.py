#!/usr/bin/env python3
"""Module for calculating likelihood of binomial data"""
import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of obtaining data given
        various hypothetical
    probabilities of developing severe side effects.
    Parameters:
    x (int): Number of patients that develop severe side effects
    n (int): Total number of patients observed
    P (numpy.ndarray): 1D array containing various hypothetical
        probabilities
    Returns:
    numpy.ndarray: 1D array containing the likelihood of obtaining
        the data
    for each probability in P
        Raises:
        ValueError: If n is not a positive integer
        ValueError: If x is not an integer >= 0
        ValueError: If x is greater than n
        TypeError: If P is not a 1D numpy.ndarray
        ValueError: If any value in P is not in range [0, 1]
    """
    # Validate n
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    # Validate x
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
            )
    # Validate x <= n
    if x > n:
        raise ValueError("x cannot be greater than n")
    # Validate P is a 1D numpy array
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    # Validate all values in P are in range [0, 1]
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    # Calculate binomial coefficient: C(n, x) = n! / (x! * (n-x)!)
    A = np.math.factorial(n)
    B = (np.math.factorial(x) * np.math.factorial(n - x))
    binomial_coef = A / B
    # binomial_coef = np.math.factorial(n) /
    # (np.math.factorial(x) * np.math.factorial(n - x))
    # Calculate likelihood using binomial probability formula:
    # L(P|x,n) = C(n,x) * P^x * (1-P)^(n-x)
    likelihood_values = binomial_coef * (P ** x) * ((1 - P) ** (n - x))
    return likelihood_values
