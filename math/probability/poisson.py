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
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def _factorial(self, n):
        """Compute factorial of n without math"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def _exp(self, x, terms=100):
        """Compute e^x using Taylor series with more terms for accuracy"""
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
        e_term = self._exp(-self.lambtha)
        result = (e_term * (self.lambtha ** k)) / self._factorial(k)
        return round(result, 10)

    def cdf(self, k):
        """This is used to find cdf for a poisson distributions"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return round(total, 10)
