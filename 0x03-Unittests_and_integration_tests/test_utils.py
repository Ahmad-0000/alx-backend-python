#!/usr/bin/env python3
"""
Contains "utils" module tests
"""
import unittest
from utils import access_nested_map, get_json
from utils import memoize as m
from parameterized import parameterized
from unittest.mock import Mock, patch


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

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, mapping, path):
        with self.assertRaises(KeyError):
            access_nested_map(mapping, path)


class TestGetJson(unittest.TestCase):
    """Testing "get_json" function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests")
    def test_get_json(self, url, payload, m_version):
        m_version.get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)
        m_version.get.use_count = m_version.get.call_count
        self.assertEqual(m_version.get.use_count, 1)


class TestMemoize(unittest.TestCase):
    """Testing memoize funcionality"""

    def test_memoize(self):
        """Testing "memozie" function"""

        class TestClass:
            """Tmeporary class"""

            def a_method(self):
                """A method to be used indirectly by 'TestClass.a_property'"""
                return 42

            @m
            def a_property(self):
                """A method to be cached"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as m_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            m_method.use_count = m_method.call_count
            self.assertEqual(m_method.use_count, 1)


if __name__ == "__main__":
    unittest.main()
