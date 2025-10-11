#!/usr/bin/env python3
"""
Binomial Distribution Module
This module contains the Binomial class that represents
The binomial distribution models the number of successes
independent Bernoulli trials.
"""


class Binomial:
    """
    Represents a binomial distribution.
    The binomial distribution is the discrete probability 
    of successes in a sequence of n independent experiments,
    question with probability p of success.
    Attributes:
        n (int): The number of Bernoulli trials
        p (float): The probability of success on each trial
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize a Binomial distribution.
        Args:
            data (list, optional): List of data to estimate the distribution.
            n (int, optional): Number of Bernoulli trials. Default is 1.
            p (float, optional): Probability of success. Default is 0.5.
        Raises:
            TypeError: If data is not a list
            ValueError: If n is not positive, p is not a valid probability,
                       or data has fewer than 2 values
        """
        if data is None:
            # Use given n and p
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            # Calculate n and p from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate mean and variance
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            # For binomial: mean = n*p and variance = n*p*(1-p)
            # From variance = n*p*(1-p) and mean = n*p:
            # variance = mean * (1-p)
            # p = 1 - variance/mean
            p = 1 - (variance / mean)
            # From mean = n*p:
            # n = mean / p
            n = mean / p
            # Round n to nearest integer
            self.n = round(n)
            # Recalculate p with the rounded n
            self.p = mean / self.n

    def pmf(self, k):
        """
        Calculate the Probability Mass Function (PMF)
        The PMF gives the probability of getting exactly
        Formula: PMF(k) = C(n,k) * p^k * (1-p)^(n-k)
        where C(n,k) is the binomial coefficient "n choose k"
        Args:
            k (int): Number of successes
        Returns:
            float: The PMF value for k, or 0 if k is out of range
        """
        # Convert k to integer if needed
        k = int(k)
        # Check if k is out of range
        if k < 0 or k > self.n:
            return 0
        # Calculate binomial coefficient C(n, k) = n! / (k! * (n-k)!)
        # Using iterative approach to avoid overflow
        binomial_coeff = 1
        for i in range(min(k, self.n - k)):
            binomial_coeff = binomial_coeff * (self.n - i) // (i + 1)
        # Calculate p^k
        p_power_k = self.p ** k
        # Calculate (1-p)^(n-k)
        q_power_n_minus_k = (1 - self.p) ** (self.n - k)
        # PMF = C(n,k) * p^k * (1-p)^(n-k)
        pmf_value = binomial_coeff * p_power_k * q_power_n_minus_k
        return pmf_value

    def cdf(self, k):
        """
        Calculate the Cumulative Distribution Function (CDF)
        The CDF gives the probability of getting at most k
        Formula: CDF(k) = sum of PMF(i) for i = 0 to k
        Args:
            k (int): Number of successes
        Returns:
            float: The CDF value for k, or 0 if k is out of range
        """
        # Convert k to integer if needed
        k = int(k)
        # Check if k is out of range
        if k < 0:
            return 0
        # If k >= n, return 1 (probability of at most n successes
        if k >= self.n:
            k = self.n
        # CDF is the sum of PMF values from 0 to k
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
