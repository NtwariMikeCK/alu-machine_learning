#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    # Axis 0: concatenate rows
    if axis == 0:
        # Check that number of columns matches
        if not mat1:
            cols1 = 0
        else:
            cols1 = len(mat1[0])
        if not mat2:
            cols2 = 0
        else:
            cols2 = len(mat2[0])
        if cols1 != cols2:
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Axis 1: concatenate columns
    elif axis == 1:
        # Check that number of rows matches
        if len(mat1) != len(mat2):
            return None
        new_matrix = []
        for row1, row2 in zip(mat1, mat2):
            new_matrix.append(row1[:] + row2[:])
        return new_matrix

    # Invalid axis
    else:
        return None
