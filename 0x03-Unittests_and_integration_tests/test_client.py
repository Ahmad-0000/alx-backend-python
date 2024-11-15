#!/usr/bin/env python3
"""
Contains tests for GithubOrgClient class
"""
import unittest
import unittest.mock
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
        with unittest.mock.patch(
                "__main__.GithubOrgClient.org",
                unittest.mock.sentinel.DEFAULT,
                None,
                False,
                None,
                None,
                unittest.mock.PropertyMock,
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

    @unittest.mock.patch("client.get_json")
    def test_public_repos(self, m_function):
        """Testing "public_repos" method"""
        m_function.return_value = [
                {
                    "payload": True,
                    "name": "Imaginary Project",
                    "license": None,
                    "repos_url": [
                        "https://github.com/my_org/imaginary"
                    ]
                }
        ]

        with unittest.mock.patch.object(
                GithubOrgClient,
                "_public_repos_url",
                unittest.mock.sentinel.DEFAULT,
                None,
                False,
                None,
                None,
                unittest.mock.PropertyMock,
                return_value={
                        "name": ["Imaginary Project"],
                        "https": "//github.com/org/imaginary"
                }):
            self.assertEqual(
                    GithubOrgClient("Imaginary")._public_repos_url["name"],
                    GithubOrgClient("Imaginary").public_repos(None)
            )


if __name__ == "__main__":
    unittest.main()
