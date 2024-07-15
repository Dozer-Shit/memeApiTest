import allure
import requests

from meme_api_tests.utils.client import MEME_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import ResponseSchemaAll


class GetAllMeme(BaseApi):
    @allure.step('Get all object')
    def get_all_meme(self, token: str) -> None:
        headers: dict = {"Authorization": token}
        self.response: requests.Response = requests.get(MEME_URL, headers=headers)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            self.validate_response(ResponseSchemaAll)
        else:
            attach_response(self.response.text, "Response")

    def check_response_is_not_empty(self) -> None:
        assert len(self.response.json()) > 0, f"Expected at least one object, got {len(self.response.json())}"
