#!/usr/bin/env python3
"""
This module provides a function to safely retrieve the first element of a list.
If the list is empty, the function returns None.
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): The list from which to get the first element.

    Returns:
        Union[Any, None]: The first element of the list if it exists, otherwise
        None.
    """
    if lst:
        return lst[0]
    else:
        return None
