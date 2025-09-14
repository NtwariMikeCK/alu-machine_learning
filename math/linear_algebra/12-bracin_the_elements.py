#!/usr/bin/env python3
"""
This module contains a function np_elementwise that performs
element-wise addition, subtraction, multiplication, and
division on NumPy arrays.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise arithmetic operations on two arrays.

    Args:
        mat1 (numpy.ndarray or scalar): First input
        mat2 (numpy.ndarray or scalar): Second input

    Returns:
        tuple: (sum, difference, product, quotient)
            - sum: element-wise addition
            - difference: element-wise subtraction
            - product: element-wise multiplication
            - quotient: element-wise division
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
