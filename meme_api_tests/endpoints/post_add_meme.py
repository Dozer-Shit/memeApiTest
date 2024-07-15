import allure
import requests

from meme_api_tests.utils.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchema


class PostAddMeme(BaseApi):
    @allure.step('Add meme object')
    def create_meme_object(self, payload: dict, token: str) -> int:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.post(MEME_URL, json=payload, headers=headers)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            self.validate_response(ResponseSchema)
            return self.valid_response.id
        else:
            attach_response(self.response.text, "Response")
