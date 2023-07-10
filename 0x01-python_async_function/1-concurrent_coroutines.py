#!/usr/bin/env python3
""" Async basics in Python task 1 """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    wait_times = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(wait_times)