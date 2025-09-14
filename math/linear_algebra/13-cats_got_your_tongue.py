s module contains a function np_cat that concatenates
two NumPy arrays along a specified axis.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two NumPy arrays along a given axis.

    Args:
        mat1 (numpy.ndarray): First array
        mat2 (numpy.ndarray): Second array
        axis (int, optional): Axis along which to concatenate.
                              Defaults to 0.

    Returns:
        numpy.ndarray: Concatenated array
    """
    return np.concatenate((mat1, mat2), axis=axis)
