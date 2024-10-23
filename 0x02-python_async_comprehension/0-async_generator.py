#!/usr/bin/env python3
"""
A simple async generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random values between 0 and 10 asyncrounously"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
