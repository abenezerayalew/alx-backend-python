#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
import time
from importlib import import_module as using


async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ Return time """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counte