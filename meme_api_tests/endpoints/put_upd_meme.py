import allure
import requests

from meme_api_tests.utils.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchema


class PutUpdMeme(BaseApi):
    @allure.step('Update meme object')
    def update_meme_object(self, payload: dict, meme_id: int, token: str) -> None:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.put(f"{MEME_URL}/{meme_id}", json=payload, headers=headers)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            self.validate_response(ResponseSchema)
        else:
            attach_response(self.response.text, "Response")

    @allure.step('Check key in response info')
    def check_does_the_answer_hold_a_key_(self, key: str) -> None:
        has_key = key in self.valid_response.info
        assert has_key, (
            f"Key {key} is present in the response info" if has_key else f"Key {key} is missing in the response info")
