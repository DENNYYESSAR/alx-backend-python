#!/usr/bin/env python3
"""
Module for creating a tuple with a string and the square of a number.

This module contains a function that takes a string and an int or float,
and returns a tuple where the first element is the string and the second
element is the square of the number, annotated as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square and include in the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k and
        the second element is the square of v.
    """
    return (k, float(v ** 2))
