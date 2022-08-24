""" 
This file contains the utility functions used in the project
"""

def rotate(in_list, n_direction):
    return in_list[n_direction:] + in_list[:n_direction]