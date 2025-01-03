#!/usr/bin/env python3
"""
Simple annotation
"""
from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns an array of "lst" items, each one is repeated "factor" times"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
