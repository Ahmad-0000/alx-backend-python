#!/usr/bin/env python3
"""
Measuring delay time
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time of wait_n divided by n"""
    t1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t2 = time.time()
    return (t2 - t1) / n
