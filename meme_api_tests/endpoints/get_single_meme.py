import allure
import requests

from meme_api_tests.utils.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchema


class GetMeme(BaseApi):
    @allure.step('Get meme object')
    def get_meme(self, meme_id: int, token: str) -> None:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.get(f"{MEME_URL}/{meme_id}", headers=headers)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            self.validate_response(ResponseSchema)
        else:
            attach_response(self.response.text, "Response")

    @allure.step('Check response id')
    def check_response_id_is_(self, meme_id) -> None:
        assert self.valid_response.id == meme_id, f"Expected id {meme_id}, got {self.valid_response.id}"
