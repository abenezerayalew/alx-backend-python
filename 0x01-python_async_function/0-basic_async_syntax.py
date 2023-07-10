#!/usr/bin/env python3
""" Async basics in Python task 0 """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay """

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
