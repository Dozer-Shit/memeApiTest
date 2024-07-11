import allure
import requests

from meme_api_tests.client import MEME_URL, validate_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchema


class PostAddMeme(BaseApi):
    @allure.step('Add meme object')
    def create_meme_object(self, payload: dict, token: str) -> int:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.post(MEME_URL, json=payload, headers=headers)
        response_json: dict = self.response.json()
        valid_response: ResponseSchema = validate_response(self, response_json, "Response", ResponseSchema)
        self.meme_id: int = valid_response.id

        return self.meme_id
