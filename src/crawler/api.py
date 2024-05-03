import requests
import colorama


class GitHubAPI_access:
    """Authenticate to github profile"""
    def __init__(self, username=str, token=str):
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        self.response = None

    def _authenticate(self):
        url = f"{self.base_url}/users/{self.username}/repos"
        headers = {"Authorization": f"token {self.token}"}

        try:
            self.response = requests.get(url, headers=headers)
            if self.response.status_code == 200:
                print(colorama.Back.GREEN,"You've been successfully connected to Github",colorama.Style.RESET_ALL)
            else:
                print(colorama.Back.RED,'Connection failed! Code:', self.response.status_code,colorama.Style.RESET_ALL)
        except:
            print(colorama.Back.RED,"Connection failed", Exception, colorama.Style.RESET_ALL)
        


class RepoList_Request(GitHubAPI_access):
    """GihHub API execution"""

    def get_repos(self):
        self._authenticate()
        if self.response.status_code == 200:
            return [repo['name'] for repo in self.response.json()]
        else:
            print(f"Failed to fetch repositories: {self.response.status_code}")
            return None