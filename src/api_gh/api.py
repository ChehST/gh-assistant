import requests



class GH_access:
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
                print("You've been successfully connected to Github")
            else:
                print('Connection failed! Code:', self.response.status_code)
        except:
            print("Connection failed", Exception)
        


class RepoList_Request(GH_access):
    """GihHub API execution"""

    def get_repos(self):
        self._authenticate()
        if self.response.status_code == 200:
            return [repo['name'] for repo in self.response.json()]
        else:
            print(f"Failed to fetch repositories: {self.response.status_code}")
            return None