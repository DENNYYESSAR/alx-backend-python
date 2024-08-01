#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.
If the key is not present, the function returns a default value.
"""

from typing import Any, TypeVar, Mapping, Union

# Define a type variable that can be any type
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    """
    Return the value for key if key is in the dictionary, else default.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None]): The value to return if the key is not found.
        Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
