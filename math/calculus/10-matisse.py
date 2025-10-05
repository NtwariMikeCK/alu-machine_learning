#!/usr/bin/env python3
"""
  Returns:
    list: List of coefficients representing the derivative of the polynomial.
    Returns [0] if the derivative is zero.
    Returns None if the input is invalid.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial represented by a list of coefficients.

    Parameters:
    poly (list): List of numbers where the index represents the power of x.
                 Example: poly = [5, 3, 0, 1] represents f(x) = 1*x^3 + 0*x^2 + 3*x + 5

    Returns:
    list: List of coefficients representing the derivative of the polynomial.
          Returns [0] if the derivative is zero.
          Returns None if the input is invalid.
    """
    # Validate input
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    # If the polynomial is constant (degree 0), derivative is zero
    if len(poly) == 1:
        return [0]

    # Compute derivative: derivative of x^i term is i*poly[i]
    derivative = [i * poly[i] for i in range(1, len(poly))]

    # If derivative is all zeros, return [0]
    if all(c == 0 for c in derivative):
        return [0]
    return derivative
