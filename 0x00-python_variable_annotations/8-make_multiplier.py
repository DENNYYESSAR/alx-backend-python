#!/usr/bin/env python3
"""
Module for creating a multiplier function.

This module contains a function that returns a new function which multiplies
a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        its product with the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the given value by the multiplier.

        Args:
            value (float): The value to multiply.

        Returns:
            float: The result of multiplying the value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
