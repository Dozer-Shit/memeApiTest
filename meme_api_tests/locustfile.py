from random import randrange, random
from locust import HttpUser, TaskSet, task, between

from tests.data.payloads import create_meme, valid_auth_payload, valid_update_payload


class UserBehavior(TaskSet):
    token: str | None = None
    meme_ids: list = []

    def on_start(self):
        if random() < 0.8:
            response = self.client.post('/authorize', json=valid_auth_payload).json()
            self.token = response['token']
        else:
            self.token = None

    def on_stop(self):
        headers = {"Authorization": self.token} if self.token else {}
        for meme_id in self.meme_ids:
            self.client.delete(f"/meme/{meme_id}", headers=headers)
        self.meme_ids.clear()

    @task(7)
    def get_meme(self):
        headers = {"Authorization": self.token} if self.token else {}
        post_id = randrange(1, 50)
        self.client.get(f"/meme/{post_id}", headers=headers)

    @task(4)
    def get_all_meme(self):
        headers = {"Authorization": self.token} if self.token else {}
        self.client.get("/meme", headers=headers)

    @task(10)
    def add_meme(self):
        if self.token:
            headers = {"Authorization": self.token}
            response = self.client.post(f"/meme", json=create_meme, headers=headers).json()
            self.meme_ids.append(response['id'])

    @task(6)
    def update_meme(self):
        if self.token and self.meme_ids:
            meme_id = self.meme_ids[-1]
            headers = {"Authorization": self.token}
            self.client.put(f"/meme/{meme_id}", json=valid_update_payload(meme_id), headers=headers)


class MemeApiUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://167.172.172.115:52355"
