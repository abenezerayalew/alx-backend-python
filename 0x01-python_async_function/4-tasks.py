#!/usr/bin/env python3
""" Async basics in Python task 4 """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ Waits for a random delay between 0 and max_delay """
    delay_list = []
    for _ in range(n):
        delay_list.append(await task_wait_random(max_delay))
    return sorted(delay_list)