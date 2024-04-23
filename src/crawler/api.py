from abc import ABC, abstractmethod
import requests


class GitHubAPI_access(ABC):
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"


class GitHubAPI_ep(GitHubAPI_access):
    """GihHub API endpont executor"""


    def get_repos(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return [repo['name'] for repo in response.json()]
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            return None