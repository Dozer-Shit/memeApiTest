import allure
import requests

from meme_api_tests.utils.client import AUTHORIZE_URL, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import TokenGetResponseSchema


class PostAuthorize(BaseApi):
    @allure.step('Authorize and get token')
    def get_token(self, payload: dict) -> str:
        self.response: requests.Response = requests.post(AUTHORIZE_URL, json=payload)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            self.validate_response(TokenGetResponseSchema)

            return self.valid_response.token
        else:
            attach_response(self.response.text, "Response")

    @allure.step('Checking the correct request name')
    def check_response_name_is_(self, name: str) -> None:
        assert name == self.valid_response.user, (f"Expected message to contain '{name}', "
                                                  + f"got {self.valid_response.user}")
