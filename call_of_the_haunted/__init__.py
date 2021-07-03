import random
import logging
import requests


def main(mytimer) -> None:
    print(requests.get(f'https://unv-shield.azurewebsites.net/api/unv_shield?code=1&txt={random.randint(0, 2**64)}').content)
