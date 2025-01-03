#!/usr/bin/env python3
"""
Contains tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock, sentinel
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand(["google", "abc"])
    @unittest.mock.patch("client.get_json")
    def test_org(self, org, m_function):
        """Testing "GithubOrgClient.org" method"""
        m_function.return_value = None
        new_org = GithubOrgClient(org)
        self.assertIsNone(new_org.org)
        m_function.once_with = m_function.assert_called_once_with
        m_function.once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Testing "_public_repos_url" method"""
        with unittest.mock.patch.object(
                GithubOrgClient,
                "org",
                sentinel.DEFAULT,
                None,
                False,
                None,
                None,
                PropertyMock,
                return_value={"payload": True, "repos_url": [
                "https://www.github.com/imaginary_org/imaginary_project_1",
                "https://www.github.com/imaginary_org/imaginary_project_2",
                ]}):
            self.assertEqual(
                GithubOrgClient("imaginary_org")._public_repos_url,
                [
                    "https://www.github.com/imaginary_org/imaginary_project_1",
                    "https://www.github.com/imaginary_org/imaginary_project_2",
                ]
            )

    @patch("client.get_json")
    def test_public_repos(self, m_fun):
        """Testing "public_repos" method"""
        m_fun.return_value = [
                {
                    "payload": True,
                    "name": "Imaginary Project",
                    "license": {
                        "name": "MIT License",
                        "key": "mit"
                    },
                    "repos_url": [
                        "https://api.github.com/org/Imaginary"
                    ]
                },
                {
                    "payload": True,
                    "name": "Imaginary Project 2",
                    "license": {
                        "name": "GNU License",
                        "key": "gnu"
                    },
                    "repos_url": [
                        "https://api.github.com/org/Imaginary"
                    ]
                },
                {
                    "payload": True,
                    "name": "Imaginary Project 3",
                    "license": {
                        "name": "MIT License",
                        "key": "mit"
                    },
                    "repos_url": [
                        "https://api.github.com/org/Imaginary"
                    ]
                }
        ]

        with patch(
                "client.GithubOrgClient._public_repos_url",
                sentinel.DEFAULT,
                None,
                False,
                None,
                None,
                PropertyMock,
                return_value=[
                    "https://api.github.com/org/Imaginary"
                ]) as m_method:
            self.assertEqual(
                    GithubOrgClient("Imaginary").public_repos("mit"),
                    ["Imaginary Project", "Imaginary Project 3"]
            )
            m_method.use_count = m_method.assert_called_once
            m_fun.use_count = m_fun.assert_called_once
            m_method.use_count()
            m_fun.use_count()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repository, key, result):
        """Testing "has_license" method"""
        self.assertEqual(GithubOrgClient.has_license(repository, key), result)

if __name__ == "__main__":
    unittest.main()
