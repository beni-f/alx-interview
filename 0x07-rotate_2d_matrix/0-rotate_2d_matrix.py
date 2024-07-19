#!/usr/bin/python3
"""
Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    """
        Solves 2d matrix rotation problem.
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    rotated_matrix = [[0] * num_cols for _ in range(num_rows)]
    

    for i in range(num_rows):
        for j in range(num_cols):
            rotated_matrix[j][num_cols - 1 - i]= matrix[i][j]

    for i in range(num_rows):
        for j in range(num_cols):
            matrix[i][j] = rotated_matrix[i][j]
