#!/usr/bin/env python3
"""
Measuring delay time
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time of wait_n divided by n"""
    t1 = time.time()
    await wait_n(n, max_delay)
    etime = time.time() - t1
    return etime / n
