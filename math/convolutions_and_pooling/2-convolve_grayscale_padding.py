#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding.
    Args:
        images: numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
        kernel: numpy.ndarray with shape (kh, kw) containing
          the convolution kernel
        padding: tuple of (ph, pw) specifying padding for
          height and width
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding
    # Pad the images with zeros using the custom padding
    padded_images = np.pad(
        images,
        pad_width=((0, 0), (ph, ph), (pw, pw)),
        mode='constant',
        constant_values=0
    )
    # Calculate output dimensions
    # After padding, the padded image has dimensions (h + 2*ph, w + 2*pw)
    # After convolution, output size = padded_size - kernel_size + 1
    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1
    # Initialize output array
    convolved = np.zeros((m, output_h, output_w))
    # Perform convolution using only two for loops
    for i in range(output_h):
        for j in range(output_w):
            # Extract the region of interest from all images at once
            # and perform element-wise multiplication with kernel, then sum
            convolved[:, i, j] = np.sum(
                padded_images[:, i:i+kh, j:j+kw] * kernel,
                axis=(1, 2)
            )
    return convolved
