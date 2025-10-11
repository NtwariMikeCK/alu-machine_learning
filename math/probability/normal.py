#!/usr/bin/env python3
"""Normal distribution class"""

import math


class Normal:
    """Represents a Normal (Gaussian) distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize a Normal distribution

        Parameters:
        - data (list): list of data to estimate the distribution
        - mean (float): mean of the distribution
        - stddev (float): standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            # Calculate mean
            self.mean = float(sum(data) / len(data))
            
            # Calculate standard deviation (population stddev)
            mean_diff_sq = [(x - self.mean) ** 2 for x in data]
            self.stddev = float(math.sqrt(sum(mean_diff_sq) / len(data)))

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
        z = (x - mean) / stddev
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score
        x = z * stddev + mean
        """
        return z * self.stddev + self.mean
    
    def pdf(self, x):
        """
        Calculates the PDF value for a given x-value
        PDF(x; μ, σ) = (1 / (σ * sqrt(2π))) * e^(-(x - μ)^2 / (2σ^2))
        """
        coefficient = 1 / (self.stddev * math.sqrt(2 * math.pi))
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        return coefficient * math.exp(exponent)
    
    def cdf(self, x):
        """Calculates the CDF value for a given x-value"""
        z = (x - self.mean) / (self.stddev * math.sqrt(2))
        return 0.5 * (1 + math.erf(z))