#!/usr/bin/env python3
"""
Contains "utils" module tests
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing "access_nested_map" function"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, mapping, path, expected):
        """Testing test_access_map method"""
        self.assertEqual(access_nested_map(mapping, path), expected)

if __name__ == "__main__":
    unittest.main()
