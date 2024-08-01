#!/usr/bin/env python3
"""
Module for computing the length of elements in a list.

This module contains a function that takes an iterable of sequences and
returns a list of tuples, where each tuple contains a sequence from the
input iterable and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each sequence in an iterable and return a list of
    tuples.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (strings, lists,
        etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
