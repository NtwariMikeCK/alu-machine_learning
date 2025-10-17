#!/usr/bin/env python3
"""Module for calculating continuous posterior probability"""
from scipy import special


def posterior(x, n, p1, p2):
    """
    Calculates the posterior probability that the probability
    # of developing
    severe side effects falls within a specific range given the data
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        p1: lower bound on the range
        p2: upper bound on the range
    Returns:
        The posterior probability that p is within the range [p1, p2]
        given x and n
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
    # Validate p1
    if not isinstance(p1, float) or p1 < 0 or p1 > 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    # Validate p2
    if not isinstance(p2, float) or p2 < 0 or p2 > 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    # Validate p2 > p1
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    # With a uniform prior (Beta(1, 1)), the posterior is Beta(x+1, n-x+1)
    # The probability that p is in [p1, p2] is the CDF difference:
    # P(p1 < p < p2) = CDF(p2) - CDF(p1)
    # Beta distribution parameters for the posterior
    alpha = x + 1
    beta = n - x + 1
    # Calculate the cumulative probability using the
    # regularized incomplete
    # beta function (which is the CDF of the Beta distribution)
    # special.betainc(a, b, x) computes I_x(a, b)
    cdf_p2 = special.betainc(alpha, beta, p2)
    cdf_p1 = special.betainc(alpha, beta, p1)
    # The posterior probability in the range [p1, p2]
    posterior_prob = cdf_p2 - cdf_p1
    return posterior_prob
