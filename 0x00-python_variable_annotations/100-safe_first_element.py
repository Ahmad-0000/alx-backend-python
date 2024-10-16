#!/usr/bin/env python3
"""
Simple Annotation
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of "lst" Sequence or None"""
    if lst:
        return lst[0]
    else:
        return None
