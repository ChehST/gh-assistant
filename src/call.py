

import requests

from crawler.api import *
from crawler.core import *

DEBUG = False

if DEBUG:
    import secrets
    username = secrets.USER
    token = secrets.GITHUB_TOKEN
else:
    print ('No Environment keys setup! Prepare for failure')
    username = ""
    token = ""



api_entrypoint = GitHubAPI_ep(username,token)
repo = RepositoryList(api_entrypoint.get_repos())
repo.print_repos()