from .api import RepoList_Request


class Repository:
    """Repositori is independent api """

    def __init__(self, name, owner=None, description=None,
                  stars=None, forks=None, license=None):
        self.name = name
        self.owner = owner
        self.description = description
        self.stars = stars
        self.forks = forks
        self.license = license

    def __str__(self):
        return f"""Repository: {self.name}\
                Owner: {self.owner}\
                Description: {self.description}\
                Stars: {self.stars}\
                Forks: {self.forks}\
                License: {self.license}"""


class RepositoryList(Repository):

    def __init__(self, repos):
        self.repos = repos
    
    def print_repos(self):
        if self.repos:
            print("Ваши репозитории:")
            for repo in self.repos:
                print(repo)
        else:
            print("Репозитории не найдены.")