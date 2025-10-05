#!/usr/bin/env python3
"""
  Calculate the derivative of a polynomial.
  
  The polynomial is represented as a list of coefficients:
  - The index of each coefficient corresponds to the power of x.
  - For example, poly = [5, 3, 0, 1] represents f(x) = 1*x^3 + 0*x^2 + 3*x + 5
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.

    The polynomial is represented as a list of coefficients:
    - Index corresponds to the power of x.
    - Example: poly = [5, 3, 0, 1] represents f(x) = 1*x^3 + 0*x^2 + 3*x + 5

    Parameters:
    poly (list): List of numbers (int or float).

    Returns:
    list: Coefficients of the derivative.
          If derivative is 0, returns [0].
          Returns None if input is invalid.
    """
    # Input validation: must be a list of numbers
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    # Constant polynomial derivative is 0
    if len(poly) == 1:
        return [0]

    # Compute derivative using list comprehension
    derivative = [i * poly[i] for i in range(1, len(poly))]

    # If derivative is all zeros, return [0]
    if all(c == 0 for c in derivative):
        return [0]

    return derivative
