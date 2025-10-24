#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.
    Args:
        images: numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
        kernel: numpy.ndarray with shape (kh, kw) containing
          the convolution kernel
    Returns:
        numpy.ndarray containing the convolved images with same dimensions as input
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    # Calculate padding needed for 'same' convolution
    # For same convolution, output size = input size
    # Padding formula: pad = (kernel_size - 1) / 2, rounded appropriately
    pad_h = kh // 2
    pad_w = kw // 2
    # Pad the images with zeros
    # pad_width format: ((before_axis0, after_axis0), (before_axis1, after_axis1), ...)
    padded_images = np.pad(
        images,
        pad_width=((0, 0), (pad_h, pad_h), (pad_w, pad_w)),
        mode='constant',
        constant_values=0
    )
    # Initialize output array with same dimensions as input
    convolved = np.zeros((m, h, w))
    # Perform convolution using only two for loops
    for i in range(h):
        for j in range(w):
            # Extract the region of interest from all images at once
            # and perform element-wise multiplication with kernel, then sum
            convolved[:, i, j] = np.sum(
                padded_images[:, i:i+kh, j:j+kw] * kernel,
                axis=(1, 2)
            )
    return convolved
