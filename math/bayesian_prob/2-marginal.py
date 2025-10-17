#!/usr/bin/env python3
"""Module for calculating marginal probability"""
import numpy as np


def marginal(x, n, P, Pr):
    """
    Calculates the marginal probability of obtaining the data
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray containing various hypothetical probabilities
        Pr: 1D numpy.ndarray containing prior beliefs about P
    Returns:
        The marginal probability of obtaining x and n
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
    # Validate P is 1D numpy array
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    # Validate Pr is numpy array with same shape as P
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    # Validate all values in P are in [0, 1]
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    # Validate all values in Pr are in [0, 1]
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    # Validate Pr sums to 1 (with tolerance for floating point errors)
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    # Calculate binomial likelihood for each probability in P
    # P(X=x | n, p) = C(n,x) * p^x * (1-p)^(n-x)
    from math import factorial
    binomial_coeff = factorial(n) / (factorial(x) * factorial(n - x))
    likelihood = binomial_coeff * (P ** x) * ((1 - P) ** (n - x))
    # Calculate marginal probability using law of total probability
    # P(X=x | n) = Σ P(X=x | n, p) * P(p)
    marginal_prob = np.sum(likelihood * Pr)
    return marginal_prob
