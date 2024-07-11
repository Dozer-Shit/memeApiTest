import allure
import requests

from meme_api_tests.client import MEME_URL, validate_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchema


class PutUpdMeme(BaseApi):
    @allure.step('Update meme object')
    def update_meme_object(self, payload: dict, meme_id: int, token) -> None:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.put(f"{MEME_URL}/{meme_id}", json=payload, headers=headers)
        response_json: dict = self.response.json()

        validate_response(self, response_json, "Response", ResponseSchema)
