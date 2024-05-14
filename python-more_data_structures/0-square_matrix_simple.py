#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    rows, cols = (6, 6)
    for i in range(rows):
        new_matrix.append([])
        for j in range(cols):
            new_matrix[i].append(matrix[i][j] * matrix[i][j])
            print(new_matrix[i][j], end=" ")
