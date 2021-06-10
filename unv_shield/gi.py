import time
from functools import lru_cache

from github import Github

from . import config


g = Github(config.gh_token)


def get_star(name):
    return _get_star(name, int(time.time())//1800)


@lru_cache(maxsize=1024)
def _get_star(name, t):
    repo = g.get_repo(name)
    return repo.stargazers_count
