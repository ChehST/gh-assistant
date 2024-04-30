import requests


class GitHubAPI_access:
    """Authenticate to github profile"""
    def __init__(self, username, token):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        self.response = None

    def _authenticate(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        headers = {"Authorization": f"token {self.token}"}
        self.response = requests.get(url, headers=headers)
        


class RepoList_Request(GitHubAPI_access):
    """GihHub API execution"""

    def get_repos(self):
        self._authenticate()
        if self.response.status_code == 200:
            return [repo['name'] for repo in self.response.json()]
        else:
            print(f"Failed to fetch repositories: {self.response.status_code}")
            return None