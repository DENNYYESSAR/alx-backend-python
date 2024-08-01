#!/usr/bin/env python3
"""
Module for calculating the floor of a floating-point number.

This module contains a function that takes a float and returns its floor value.
"""

import math


def floor(n: float) -> int:
    """
    Calculate the floor of a floating-point number.

    Args:
        n (float): The number to find the floor of.

    Returns:
        int: The floor of the number.
    """
    return math.floor(n)
