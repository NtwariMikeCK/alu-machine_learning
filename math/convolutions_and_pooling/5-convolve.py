#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images using multiple kernels.
    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing
          multiple images
        kernels: numpy.ndarray with shape (kh, kw, c, nc)
          containing the kernels
        padding: either a tuple of (ph, pw), 'same',
          or 'valid'
        stride: tuple of (sh, sw) specifying stride for
          height and width
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
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
    # Output has nc channels (one for each kernel)
    convolved = np.zeros((m, output_h, output_w, nc))
    # Perform convolution using three for loops
    for i in range(output_h):
        for j in range(output_w):
            for k in range(nc):
                # Calculate the starting position in the padded image
                start_i = i * sh
                start_j = j * sw
                # Extract the region of interest from all images at once
                # Shape: (m, kh, kw, c)
                region = padded_images[:, start_i:start_i+kh, start_j:start_j+kw, :]
                # Get the k-th kernel
                # Shape: (kh, kw, c)
                kernel = kernels[:, :, :, k]
                # Perform element-wise multiplication with kernel and sum
                # Sum over kernel height, kernel width, and channels
                convolved[:, i, j, k] = np.sum(
                    region * kernel,
                    axis=(1, 2, 3)
                )
    return convolved
