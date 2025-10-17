#!/usr/bin/env python3
"""Module for calculating posterior probability"""
import numpy as np


def posterior(x, n, P, Pr):
    """
    Calculates the posterior probability for the various hypothetical
    probabilities of developing severe side effects given the data
    Args:
        x: number of patients that develop severe side effects
        n: total number of patients observed
        P: 1D numpy.ndarray containing various hypothetical probabilities
        Pr: 1D numpy.ndarray containing prior beliefs about P
    Returns:
        The posterior probability of each probability in P given x and n
    """
    # Import the intersection and marginal functions
    intersection = __import__('1-intersection').intersection
    marginal = __import__('2-marginal').marginal
    # Calculate the intersection for all probabilities
    # This handles all validation internally
    intersection_values = intersection(x, n, P, Pr)
    # Calculate the marginal probability (evidence)
    marginal_prob = marginal(x, n, P, Pr)
    # Calculate posterior using Bayes' theorem:
    # P(p|x,n) = P(x,n|p) * P(p) / P(x,n)
    #          = intersection / marginal
    posterior_prob = intersection_values / marginal_prob
    return posterior_prob
