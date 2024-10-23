#!/usr/bin/env python3
"""
Using tasks
"""
import asyncio
import typing
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of the delays in ascending order without using 'sort'"""
    res = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for i in asyncio.as_completed(tasks):
        c = await i
        res.append(c)
    return res
