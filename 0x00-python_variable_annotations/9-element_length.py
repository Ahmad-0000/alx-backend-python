#!/usr/bin/env python3
"""
Simple Annotation
"""
from typing import List, Sequence, Tuple


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of an item from sequence and its length"""
    return [(i, len(i)) for i in lst]
