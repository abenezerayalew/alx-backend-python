#!/usr/bin/env python3
""" Async Comprehensions """
from typing import List
from importlib import import_module as using


async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Return list of random numbers """
    return [i async for i in async_generator()]
