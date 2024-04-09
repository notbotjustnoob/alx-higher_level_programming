#!/usr/bin/python3
"""
Module to print text with indentation
"""

def text_indentation(text):
    """
    Function to print text with 2 new lines after '.', '?' and ':'
    
    Args:
        text (str): Text to be indented
    
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    start = 0
    for i in range(len(text)):
        if text[i] in chars:
            print(text[start:i + 1].strip())
            print()
            start = i + 1
    print(text[start:].strip())
