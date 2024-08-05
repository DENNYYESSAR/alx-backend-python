#!/usr/bin/env python3
"""
This module provides an asynchronous function that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the
    delay.

    :param max_delay: Maximum delay in seconds (default is 10).
    :return: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
