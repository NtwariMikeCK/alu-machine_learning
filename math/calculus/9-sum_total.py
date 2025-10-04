#!/usr/bin/env python3
"""
   Calculate the sum of squares of the first n natural numbers.
   Uses the formula: 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2n+1)/6
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares of the first n natural numbers.

    Uses the formula: 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2n+1)/6

    Parameters:
    n (int): The number up to which to sum squares. Must be a positive integer.

    Returns:
    int: The sum of squares from 1 to n.
    None: If n is not a valid positive integer.
    """
    # Validate input: must be an integer greater than or equal to 1
    if not isinstance(n, int) or n < 1:
        return None

    # Use the formula to calculate sum of squares
    return n * (n + 1) * (2 * n + 1) // 6
