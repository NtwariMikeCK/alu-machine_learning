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
    - The index of each coefficient corresponds to the power of x.
    - For example, poly = [5, 3, 0, 1] represents f(x) = 1*x^3 + 0*x^2 + 3*x + 5

    Parameters:
    poly (list): List of numbers (int or float) representing polynomial coefficients.

    Returns:
    list: A new list of coefficients representing the derivative of the polynomial.
          If the derivative is 0, returns [0].
          Returns None if the input is not a valid list of numbers.
    """
    # Validate input
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    # If the polynomial is constant (degree 0), derivative is 0
    if len(poly) == 1:
        return [0]

    # Compute derivative: coefficient for x^i becomes i*poly[i]
    derivative = [i * poly[i] for i in range(1, len(poly))]

    # If derivative is all zeros, return [0]
    if all(c == 0 for c in derivative):
        return [0]

    return derivative
