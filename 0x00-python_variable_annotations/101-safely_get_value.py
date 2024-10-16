#!/usr/bin/env python3
"""
Simple Annotation
"""
from typing import TypeVar, Mapping, Optional, Union, Dict, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Returns an a value associated with "key" if "key" is a key in
    "dct", else "default"
    """
    if key in dct:
        return dct[key]
    else:
        return default
