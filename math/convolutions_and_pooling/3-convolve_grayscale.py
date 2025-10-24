#!/usr/bin/env python3
"""Performs a valid convolution on grayscale images."""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on grayscale images
    Args:
        images: numpy.ndarray with shape (m, h, w)
        kernel: numpy.ndarray with shape (kh, kw)
        padding: either a tuple of (ph, pw), 'same', or 'valid'
        stride: tuple of (sh, sw)
    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    # Determine padding
    if type(padding) == tuple:
        ph, pw = padding
    elif padding == 'same':
        # Formula ensures output height and width equal input
        ph = int((((h - 1) * sh + kh - h) / 2))
        pw = int((((w - 1) * sw + kw - w) / 2))
    elif padding == 'valid':
        ph, pw = (0, 0)
    else:
        raise ValueError("padding must be 'same', 'valid', or a tuple")
    # Pad images
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), mode='constant')
    # Compute output dimensions
    oh = ((h + 2 * ph - kh) // sh) + 1
    ow = ((w + 2 * pw - kw) // sw) + 1
    # Prepare output
    output = np.zeros((m, oh, ow))
    # Convolution with only two loops
    for i in range(oh):
        for j in range(ow):
            region = padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw]
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))
    return output
