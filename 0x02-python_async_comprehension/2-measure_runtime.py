#!/usr/bin/env python3
"""
Measuring runtime
"""
import asyncio
import time


ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns total execution time"""
    time1 = time.time()
    await asyncio.gather(*[asyncio.create_task(ac()) for i in range(4)])
    time2 = time.time()
    return time2 - time1
