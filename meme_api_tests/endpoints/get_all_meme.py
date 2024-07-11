import allure
import requests

from meme_api_tests.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi


class GetAllMeme(BaseApi):
    @allure.step('Get all object')
    def get_all_meme(self, token: str) -> None:
        headers = {"Authorization": token}
        self.response: requests.Response = requests.get(MEME_URL, headers=headers)
        # attach_response(self.response, "Response")
        self.response_json: dict = self.response.json()

    def check_response_is_not_empty(self) -> tuple[bool, str]:
        return len(self.response_json) > 0, f"Expected at least one object, got {len(self.response_json)}"
