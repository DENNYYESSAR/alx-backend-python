#!/usr/bin/env python3
"""
Module for summing a list of floating-point numbers.

This module contains a function that takes a list of floats and returns their
sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum the elements of a list of floating-point numbers.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
