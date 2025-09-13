#!/usr/bin/env python3
def matrix_transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):       # loop over columns
        new_row = []
        for row in matrix:          # collect each row’s i-th element
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed
