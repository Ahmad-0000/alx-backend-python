#!/usr/bin/env python3
"""
Concurrent awaitables
"""
import asyncio
import typing
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """Returns a list of the delays in ascending order without using 'sort'"""
    res = []
    for i in asyncio.as_completed([wait_random(max_delay) for n in range(n)]):
        c = await i
        res.append(c)
    return res
