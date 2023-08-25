from locust import HttpUser, task, between


class GuestUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def visit_index_handler(self):
        self.client.get("/")

    @task
    def visit_concurrency_handler(self):
        self.client.get("/error")

    @task
    def visit_slo_handler(self):
        self.client.get("/slo")
