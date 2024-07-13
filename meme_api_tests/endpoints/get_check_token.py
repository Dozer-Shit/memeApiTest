import allure
import requests

from meme_api_tests.client import AUTHORIZE_URL

from meme_api_tests.endpoints.base_api import BaseApi


class GetCheckToken(BaseApi):
    @allure.step('Check token is valid')
    def check_token_is_valid(self, token: str) -> None:
        self.response: requests.Response = requests.get(f"{AUTHORIZE_URL}/{token}")
        # attach_response(self.response, "Response")
