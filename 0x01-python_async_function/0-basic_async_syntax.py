#!/usr/bin/env python3
"""
Experiencing the async/await syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Delays for a random seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
