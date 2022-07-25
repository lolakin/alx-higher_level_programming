#!/usr/bin/python3
"""
Module print_square
Prints a square with '#' char
"""

def print_square(size):
    """Prints a square with it's 
    length and width as size
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for i in range(size):
            print('#','')
        print()
