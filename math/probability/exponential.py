#!/usr/bin/env python3
"""
Exponential distribution class
"""


class Exponential:
    """Represents an Exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize an Exponential distribution

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
            # For exponential distribution, lambtha is 1 / mean
            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)

    def _exp(self, x, terms=100):
        """Compute e^x using Taylor series expansion"""
        result = 1.0
        term = 1.0
        for i in range(1, terms):
            term *= x / i
            result += term
        return result

    def pdf(self, x):
        if x < 0:
            return 0
        # use larger terms for stability
        return self.lambtha * self._exp(-self.lambtha * x, terms=150)

    def cdf(self, x):
        if x < 0:
            return 0
        return 1 - self._exp(-self.lambtha * x, terms=150)
