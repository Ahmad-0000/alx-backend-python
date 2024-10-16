#!/usr/bin/env python3
"""
More advanced annotation
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of two elements, k and the square of v as a float"""
    return (k, float(v ** 2))
