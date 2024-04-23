from .api import GitHubAPI_ep



class Repository:

    def __init__(self,name):
        self.name = name


class RepositoryList(Repository,GitHubAPI_ep):

    def __init__(self, repos):
        self.repos = repos
    
    def print_repos(self):
        if self.repos:
            print("Ваши репозитории:")
            for repo in self.repos:
                print(repo)
        else:
            print("Репозитории не найдены.")