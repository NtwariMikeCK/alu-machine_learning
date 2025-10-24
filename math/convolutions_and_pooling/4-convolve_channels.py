#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images with channels.
    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing
          multiple images
        kernel: numpy.ndarray with shape (kh, kw, c) containing
          the convolution kernel
        padding: either a tuple of (ph, pw), 'same', or 'valid'
        stride: tuple of (sh, sw) specifying stride for
          height and width
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
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
    # Only pad height and width dimensions, not the channel dimension
    padded_images = np.pad(
        images,
        pad_width=((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode='constant',
        constant_values=0
    )
    # Calculate output dimensions with stride
    output_h = (h + 2 * ph - kh) // sh + 1
    output_w = (w + 2 * pw - kw) // sw + 1
    # Initialize output array
    # Note: output has no channel dimension (collapses to single value per position)
    convolved = np.zeros((m, output_h, output_w))
    # Perform convolution using only two for loops
    for i in range(output_h):
        for j in range(output_w):
            # Calculate the starting position in the padded image
            start_i = i * sh
            start_j = j * sw
            # Extract the region of interest from all images at once
            # Shape: (m, kh, kw, c)
            region = padded_images[:, start_i:start_i+kh, start_j:start_j+kw, :]
            # Perform element-wise multiplication with kernel and sum over all dimensions
            # except the batch dimension
            # This sums across kernel height, kernel width, AND channels
            convolved[:, i, j] = np.sum(
                region * kernel,
                axis=(1, 2, 3)
            )
    return convolved
