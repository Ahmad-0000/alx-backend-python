#!/usr/bin/env python3
"""
Contains tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org, m_function):
        """Testing "GithubOrgClient.org" method"""
        m_function.return_value = {"payload": True}
        new_org = GithubOrgClient(org)
        self.assertEqual(new_org.org, {"payload": True})
        m_function.once_with = m_function.assert_called_once_with
        m_function.once_with(f"https://api.github.com/orgs/{org}")


if __name__ == "__main__":
    unittest.main()
