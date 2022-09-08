"""
This file contains the utility functions used in the project
"""

def rotate(in_list, n_direction):
    """
    Wrapper to rotate list depending on the input direction
    and number of places.
    """
    return in_list[n_direction:] + in_list[:n_direction]
