#!/usr/bin/env python3
""" Async basics in Python task 0 """
def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and max_delay """
    import random
    import asyncio
    delay = random.uniform(0, max_delay)
    asyncio.sleep(delay)
    return delay
