#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on grayscale images.
    Args:
        images: numpy.ndarray with shape (m, h, w) containing
            multiple grayscale images
        kernel: numpy.ndarray with shape (kh, kw) containing
            the convolution kernel
        padding: either a tuple of (ph, pw), 'same', or 'valid'
        stride: tuple of (sh, sw) specifying stride for height
            and width
    
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    # Determine padding based on the padding parameter
    if padding == 'same':
        # Calculate padding needed for 'same' convolution
        ph = kh // 2
        pw = kw // 2
    elif padding == 'valid':
        # No padding for 'valid' convolution
        ph = 0
        pw = 0
    else:
        # Custom padding provided as tuple
        ph, pw = padding
    # Pad the images with zeros
    padded_images = np.pad(
        images,
        pad_width=((0, 0), (ph, ph), (pw, pw)),
        mode='constant',
        constant_values=0
    )
    # Calculate output dimensions with stride
    # Formula: output_size = (input_size + 2*padding - kernel_size)
    # / stride + 1
    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1
    # Initialize output array
    convolved = np.zeros((m, output_h, output_w))
    # Perform convolution using only two for loops
    for i in range(output_h):
        for j in range(output_w):
            # Calculate the starting position in the padded image
            # taking stride into account
            start_i = i * sh
            start_j = j * sw
            # Extract the region of interest from all images at once
            # and perform element-wise multiplication with kernel, then sum
            convolved[:, i, j] = np.sum(
                padded_images[:, start_i:start_i+kh, start_j:start_j+kw] * kernel,
                axis=(1, 2)
            )
    return convolved
