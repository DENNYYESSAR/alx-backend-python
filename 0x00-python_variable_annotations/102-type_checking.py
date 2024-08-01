#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by repeating its
elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zoom into an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The number of times to repeat each element. Defaults to
        2.
i
    Returns:
        Tuple[int, ...]: A new tuple with elements repeated.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)  # Changed from list to tuple to match the type hint

zoom_2x = zoom_array(array)

# Corrected the factor to be an integer
zoom_3x = zoom_array(array, 3)
