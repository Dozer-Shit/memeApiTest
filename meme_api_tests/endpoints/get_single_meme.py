import allure
import requests

from meme_api_tests.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi


class GetMeme(BaseApi):
    @allure.step('Get object')
    def get_meme(self, meme_id: int, token: str) -> None:
        headers = {"Authorization": token}
        self.response: requests.Response = requests.get(f"{MEME_URL}/{meme_id}", headers=headers)
        # attach_response(self.response, "Response")
        self.response_json: dict = self.response.json()

    @allure.step('Check response id')
    def check_response_id_is_(self, meme_id) -> tuple[bool, str]:
        return self.response_json['id'] == meme_id, f"Expected id {meme_id}, got {self.response_json['id']}"
