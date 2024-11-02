from functools import lru_cache

import requests


class PeopleRepository:
    BASE_URL = "https://swapi.dev/api/people/"

    @staticmethod
    @lru_cache(maxsize=100)
    def get_all_people():
        response = requests.get(PeopleRepository.BASE_URL)
        response.raise_for_status()
        return response.json()
