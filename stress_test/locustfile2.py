from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def index(self):
        self.client('/')

    @task(3)
    def predict(self):
        self.client.posty('/predict', params={'text':'dolar'})


class APIUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
