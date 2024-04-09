#!/usr/bin/python3
"""
Module to print a square
"""

def print_square(size):
    """
    Function to print a square with the character #
    
    Args:
        size (int): Size length of the square
    
    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
