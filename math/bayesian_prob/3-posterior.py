#!/usr/bin/env python3
"""Module for calculating posterior probability"""
import numpy as np


def posterior(x, n, P, Pr):
    """
    Calculates the posterior probability for the various hypothetical
    probabilities of developing severe side effects given the data.
    Parameters:
    x (int): Number of patients that develop severe side effects
    n (int): Total number of patients observed
    P (numpy.ndarray): 1D array containing various hypothetical probabilities
    Pr (numpy.ndarray): 1D array containing prior beliefs of P
    Returns:
    numpy.ndarray: 1D array containing the posterior probability of each
                   probability in P given x and n
    Raises:
    ValueError: If n is not a positive integer
    ValueError: If x is not an integer >= 0
    ValueError: If x is greater than n
    TypeError: If P is not a 1D numpy.ndarray
    TypeError: If Pr is not a numpy.ndarray with same shape as P
    ValueError: If any value in P is not in range [0, 1]
    ValueError: If any value in Pr is not in range [0, 1]
    ValueError: If Pr does not sum to 1
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
    # Validate Pr is a numpy array with same shape as P
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    # Validate all values in P are in range [0, 1]
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    # Validate all values in Pr are in range [0, 1]
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    # Validate Pr sums to 1
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    # Calculate binomial coefficient: C(n, x) = n! / (x! * (n-x)!)
    A = np.math.factorial(n)
    B = (np.math.factorial(x) * np.math.factorial(n - x))
    # binomial_coef = np.math.factorial(n) /
    # (np.math.factorial(x) * np.math.factorial(n - x))
    # Calculate likelihood using binomial probability formula:
    # L(P|x,n) = C(n,x) * P^x * (1-P)^(n-x)
    likelihood_values = binomial_coef * (P ** x) * ((1 - P) ** (n - x))
    # Calculate intersection: Likelihood * Prior
    intersection_values = likelihood_values * Pr
    # Calculate marginal probability: sum of all intersections
    marginal_prob = np.sum(intersection_values)
    # Calculate posterior probability using Bayes' theorem:
    # P(P|x,n) = P(x,n|P) * P(P) / P(x,n)
    #          = Intersection / Marginal
    posterior_prob = intersection_values / marginal_prob
    return posterior_prob
