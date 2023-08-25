from locust import HttpUser, task, between


class GuestUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def visit_index_handler(self):
        self.client.get("/")

    @task(2)
    def visit_concurrency_handler(self):
        self.client.get("/error")
