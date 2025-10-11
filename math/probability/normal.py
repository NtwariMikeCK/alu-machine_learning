#!/usr/bin/env python3
"""
Normal Distribution Module
This module contains the Normal class that represents
The normal distribution is the most probability
"""


class Normal:
    """
    Represents a normal (Gaussian) distribution.
    The normal distribution is a continuous probability
    symmetric around its mean, showing that data near the mean
    in occurrence than data far from the mean.
    Attributes:
        mean (float): The mean (average) of the distribution
        stddev (float): The standard deviation of the distribution
    """
    
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize a Normal distribution.
        Args:
            data (list, optional): List of data to estimate
            mean (float, optional): Mean of the distribution. Default is 0.
            stddev (float, optional): Standard deviation. Default is 1.
        Raises:
            TypeError: If data is not a list
            ValueError: If stddev is not positive or data has fewer than 2 values
        """
        if data is None:
            # Use given mean and stddev
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            # Calculate mean and stddev from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate mean
            self.mean = sum(data) / len(data)
            # Calculate standard deviation
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5
    
    def z_score(self, x):
        """
        Calculate the z-score of a given x-value.
        The z-score indicates how many standard deviations an element
        Formula: z = (x - mean) / stddev
        Args:
            x (float): The x-value
        Returns:
            float: The z-score of x
        """
        return (x - self.mean) / self.stddev
    
    def x_value(self, z):
        """
        Calculate the x-value of a given z-score.
        This is the inverse of the z-score calculation.
        Formula: x = mean + z * stddev
        Args:
            z (float): The z-score
        Returns:
            float: The x-value of z
        """
        return self.mean + z * self.stddev
    
    def pdf(self, x):
        """
        Calculate the Probability Density Function (PDF) for a given x-value.
        The PDF gives the relative likelihood for the random variable to take on
        a given value.
        Formula: PDF(x) = (1 / (stddev * sqrt(2*pi))) * e^(-0.5 * ((x - mean) / stddev)^2)
        Args:
            x (float): The x-value
        Returns:
            float: The PDF value for x
        """
        # Constants
        pi = 3.1415926536
        e = 2.7182818285
        # Calculate the coefficient: 1 / (stddev * sqrt(2*pi))
        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)
        # Calculate the exponent: -0.5 * ((x - mean) / stddev)^2
        z_score = (x - self.mean) / self.stddev
        exponent = -0.5 * (z_score ** 2)
        # PDF = coefficient * e^exponent
        pdf_value = coefficient * (e ** exponent)
        return pdf_value
    
    def cdf(self, x):
        """
        Calculate the Cumulative Distribution Function (CDF) for a given x-value.
        The CDF gives the probability that the random variable is less than or
        equal to a certain value x.
        Formula: CDF(x) = 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))))
        where erf is the error function
        Args:
            x (float): The x-value
        Returns:
            float: The CDF value for x
        """
        # Calculate z-score
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        # Calculate error function using Taylor series approximation
        # erf(z) ≈ (2/sqrt(pi)) * (z - z^3/3 + z^5/10 - z^7/42 + z^9/216 - ...)
        pi = 3.1415926536
        # Taylor series for erf
        erf_value = z
        term = z
        for n in range(1, 100):
            term *= -z * z / n
            erf_value += term / (2 * n + 1)
        erf_value *= 2 / (pi ** 0.5)
        # CDF = 0.5 * (1 + erf(z))
        cdf_value = 0.5 * (1 + erf_value)
        return cdf_value
