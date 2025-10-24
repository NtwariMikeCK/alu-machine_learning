#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.
    Args:
        images: numpy.ndarray with shape (m, h, w) containing
            multiple grayscale images
        kernel: numpy.ndarray with shape (kh, kw) containing
            the convolution kernel
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    # Calculate output dimensions for valid convolution
    output_h = h - kh + 1
    output_w = w - kw + 1
    # Initialize output array
    convolved = np.zeros((m, output_h, output_w))
    # Perform convolution using only two for loops
    for i in range(output_h):
        for j in range(output_w):
            # Extract the region of interest from all images at once
            # and perform element-wise multiplication with kernel, then sum
            convolved[:, i, j] = np.sum(
                images[:, i:i+kh, j:j+kw] * kernel,
                axis=(1, 2)
            )
    return convolved
