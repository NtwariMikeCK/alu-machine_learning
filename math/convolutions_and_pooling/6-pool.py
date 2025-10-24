#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images.
    Args:
        images: numpy.ndarray with shape (m, h, w, c) containing
          multiple images
        kernel_shape: tuple of (kh, kw) containing the kernel
          shape for pooling
        stride: tuple of (sh, sw) specifying stride for
          height and width
        mode: 'max' for max pooling or 'avg' for average
          pooling
    Returns:
        numpy.ndarray containing the pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride
    # Calculate output dimensions
    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1
    # Initialize output array
    pooled = np.zeros((m, output_h, output_w, c))
    # Perform pooling using only two for loops
    for i in range(output_h):
        for j in range(output_w):
            # Calculate the starting position in the image
            start_i = i * sh
            start_j = j * sw
            # Extract the region of interest from all images and all channels
            # Shape: (m, kh, kw, c)
            region = images[:, start_i:start_i+kh, start_j:start_j+kw, :]
            # Apply pooling operation
            if mode == 'max':
                # Max pooling: take maximum value in each window
                pooled[:, i, j, :] = np.max(region, axis=(1, 2))
            elif mode == 'avg':
                # Average pooling: take mean value in each window
                pooled[:, i, j, :] = np.mean(region, axis=(1, 2))
    return pooled
