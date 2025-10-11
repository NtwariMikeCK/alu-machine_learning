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
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def _exp(self, x, terms=100):
        """Compute e^x using Taylor series expansion with more terms"""
        result = 1.0
        term = 1.0
        for i in range(1, terms):
            term *= x / i
            result += term
        return result

    def pmf(self, k):
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return (self._exp(-self.lambtha) * (self.lambtha ** k)) / self._factorial(k)

    def cdf(self, k):
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
