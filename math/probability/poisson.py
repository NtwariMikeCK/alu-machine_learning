#!/usr/bin/env python3
"""
Poisson distribution class
"""


class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize a Poisson distribution

        Parameters:
        - data (list): list of data to estimate the distribution
        - lambtha (float): expected number of occurrences
        """
        if data is None:
            # Use provided lambtha
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # Validate data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate lambtha as mean of data
            self.lambtha = float(sum(data) / len(data))

    def _factorial(self, n):
        """Compute factorial of n """
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def _exp(self, x, terms=20):
        """Compute e^x using Taylor series expansion"""
        result = 1.0
        numerator = 1.0
        denominator = 1.0
        for i in range(1, terms):
            numerator *= x
            denominator *= i
            result += numerator / denominator
        return result

    def pmf(self, k):
        """
        Calculates the PMF value for a given number of successes (k)
        PMF(k; λ) = (e^(-λ) * λ^k) / k!
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        e_term = self._exp(-self.lambtha)
        fact_term = self._factorial(k)
        pmf = (e_term * (self.lambtha ** k)) / fact_term
        return pmf

    def cdf(self, k):
        """
        Calculates the CDF value for a given number of successes
        CDF(k; λ) = sum_{i=0}^{k} PMF(i; λ)
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
