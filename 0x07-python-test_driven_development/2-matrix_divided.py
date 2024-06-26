#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Function to divide all elements of a matrix
    
    Args:
        matrix (list of list): Matrix of integers or floats
        div (int or float): Divisor
    
    Returns:
        list of list: New matrix with elements divided by div
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
