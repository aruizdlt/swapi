from locust import HttpUser, task, constant


class DemoUser(HttpUser):
    # Simula el comportamiento de los usuarios con un tiempo de espera entre tareas
    wait_time = constant(1)

    @task
    def get_all_people(self):
        self.client.get("/people")

    @task
    def get_sorted_people(self):
        self.client.get("/people/names-sorted")
