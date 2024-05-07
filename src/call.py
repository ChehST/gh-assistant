from api_assistent.api import *
from api_gh.api import *

DEBUG = True

if DEBUG:
    import secrets
    username = secrets.USER
    token = secrets.GITHUB_TOKEN
else:
    print ('No Environment keys setup! Prepare for failure')
    username = ""
    token = ""

gh_api = RepoList_Request(username,token)
repo = RepositoryList(gh_api.get_repos())
repo.print_repos()