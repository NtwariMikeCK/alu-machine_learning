#!/usr/bin/env python3
"""Binomial distribution class"""

import math


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize a Binomial distribution"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean_data = sum(data) / len(data)
            var_data = sum((x - mean_data) ** 2 for x in data) / len(data)

            p_est = 1 - (var_data / mean_data) if mean_data != 0 else 0
            if p_est <= 0 or p_est >= 1:
                raise ValueError("data does not allow valid estimation of p")

            n_est = round(mean_data / p_est)
            p_est = mean_data / n_est if n_est != 0 else 0

            self.n = int(n_est)
            self.p = float(p_est)

    def pmf(self, k):
        """Calculates the PMF value for a given number of successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0

        comb = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the CDF value for a given number of successes"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        if k > self.n:
            k = self.n

        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value
