#!/usr/bin/env python3
"""
Exponential Distribution Module
This module contains the Exponential class that
The exponential distribution models the time
"""


class Exponential:
    """
    Represents an exponential distribution.
    The exponential distribution is used to model
    occur continuously and independently at a
    Attributes:
        lambtha (float): The rate parameter (numbe
    """
    def __init__(self, data=None, lambtha=1.):
        """
        Initialize an Exponential distribution.
        Args:
            data (list, optional): List of data to estimate the
            lambtha (float, optional): Rate parameter. Default is 1.
        Raises:
            TypeError: If data is not a list
            ValueError: If lambtha is not positive or data
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
            # For exponential distribution, lambtha = 1 / mean
            mean = sum(data) / len(data)
            self.lambtha = 1 / mean

    def pdf(self, x):
        """
        Calculate the Probability Density Function (PDF) for a
        The PDF gives the relative likelihood for the
        Formula: PDF(x) = lambtha * e^(-lambtha * x)
        Args:
            x (float): Time period
        Returns:
            float: The PDF value for x, or 0 if x is out of range
        """
        # Check if x is out of range (negative)
        if x < 0:
            return 0
        # Calculate e^(-lambtha * x)
        e = 2.7182818285
        exp_value = e ** (-self.lambtha * x)
        # PDF = lambtha * e^(-lambtha * x)
        pdf_value = self.lambtha * exp_value
        return pdf_value

    def cdf(self, x):
        """
        Calculate the Cumulative Distribution
        The CDF gives the probability that the
        equal to a certain value x.
        Formula: CDF(x) = 1 - e^(-lambtha * x)
        Args:
            x (float): Time period
        Returns:
            float: The CDF value for x, or 0 if x is out of range
        """
        # Check if x is out of range (negative)
        if x < 0:
            return 0
        # Calculate e^(-lambtha * x)
        e = 2.7182818285
        exp_value = e ** (-self.lambtha * x)
        # CDF = 1 - e^(-lambtha * x)
        cdf_value = 1 - exp_value
        return cdf_value
