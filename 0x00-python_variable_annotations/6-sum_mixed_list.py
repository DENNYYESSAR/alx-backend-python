#!/usr/bin/env python3
"""
Module for summing a list of integers and floating-point numbers.

This module contains a function that takes a list of integers and
floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum the elements of a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats
        to sum.

    Returns:
        float: The sum of the list elements.
    """
    return float(sum(mxd_lst))
