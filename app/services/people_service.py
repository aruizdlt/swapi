from app.models.person_model import Person
from app.repositories.people_repository import PeopleRepository


class PeopleService:
    @staticmethod
    def get_people():
        data = PeopleRepository.get_all_people()
        people_list = [Person(**person) for person in data["results"]]
        return people_list

    @staticmethod
    def get_people_names_sorted():
        data = PeopleRepository.get_all_people()
        names = [person["name"] for person in data["results"]]
        return sorted(names)
