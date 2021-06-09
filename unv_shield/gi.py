import time
from functools import lru_cache

from github import Github


g = Github()


def get_star(name):
    return _get_star(name, int(time.time())//600)


@lru_cache(maxsize=1024)
def _get_star(name, t):
    repo = g.get_repo(name)
    return repo.stargazers_count
