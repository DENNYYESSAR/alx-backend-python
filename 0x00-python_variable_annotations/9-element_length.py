#!/usr/bin/env python3
"""
Module for computing the length of elements in a list.

This module contains a function that takes a list of strings and returns
a list of tuples, where each tuple contains an element from the input list
and its length.
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Compute the length of each string in a list and return a list of tuples.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains a
        string from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
