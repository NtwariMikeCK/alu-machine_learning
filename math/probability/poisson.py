#!/usr/bin/env python3
"""
Poisson Distribution Module
This module contains the Poisson class that represents
The Poisson distribution models the probability of a
occurring in a fixed interval of time or space.
"""


class Poisson:
    """
    Represents a Poisson distribution.
    The Poisson distribution is used to model
    in a fixed interval of time or space when these
    constant mean rate and independently of the time since
    Attributes:
        lambtha (float): The expected number of occurrences
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize a Poisson distribution.
        Args:
            data (list, optional): List of data to estimate the distribution.
            lambtha (float, optional): Expected number of occurrences.
        Raises:
            TypeError: If data is not a list
            ValueError: If lambtha is not positive or data has fewer than
        """
        if data is None:
            # Use given lambtha
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # Calculate lambtha from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Lambtha is the mean of the data for Poisson distribution
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculate the Probability Mass Function (PMF) for a given number
        The PMF gives the probability that a discrete random variable
        equal to some value k.
        Formula: PMF(k) = (lambtha^k * e^(-lambtha)) / k!
        Args:
            k (int): Number of successes (occurrences)
        Returns:
            float: The PMF value for k, or 0 if k is out of range
        """
        # Convert k to integer if needed
        k = int(k)
        # Check if k is out of range (negative)
        if k < 0:
            return 0
        # Calculate e^(-lambtha)
        e = 2.7182818285
        exp_neg_lambtha = e ** (-self.lambtha)
        # Calculate lambtha^k
        lambtha_power_k = self.lambtha ** k
        # Calculate k! (factorial)
        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i
        # PMF = (lambtha^k * e^(-lambtha)) / k!
        pmf_value = (lambtha_power_k * exp_neg_lambtha) / k_factorial
        return pmf_value

    def cdf(self, k):
        """
        Calculate the Cumulative Distribution Function (CDF)
        The CDF gives the probability that a random variable is less
        to a certain value k.
        Formula: CDF(k) = sum of PMF(i) for i = 0 to k
        Args:
            k (int): Number of successes (occurrences)
        Returns:
            float: The CDF value for k, or 0 if k is out of range
        """
        # Convert k to integer if needed
        k = int(k)
        # Check if k is out of range (negative)
        if k < 0:
            return 0
        # CDF is the sum of PMF values from 0 to k
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
