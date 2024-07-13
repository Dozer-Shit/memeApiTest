import allure
import requests

from meme_api_tests.client import AUTHORIZE_URL, validate_response, attach_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import TokenGetResponseSchema


class PostAuthorize(BaseApi):
    @allure.step('Authorize and get token')
    def get_token(self, payload: dict) -> str:
        self.response: requests.Response = requests.post(AUTHORIZE_URL, json=payload)
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            attach_response(self.response.json(), "Response")
            response_json: dict = self.response.json()
            valid_response: TokenGetResponseSchema = validate_response(self, response_json, TokenGetResponseSchema)
            self.token: str = valid_response.token

            return self.token
        else:
            attach_response(self.response.text, "Response")

    @allure.step('Checking the correct request name')
    def check_response_name_is_(self, name: str) -> tuple[bool, str]:
        return name == self.valid_response.user, (f"Expected message to contain '{name}', "
                                                  + f"got {self.valid_response.user}")

    @allure.step('Checking the response message')
    def check_response_message_is_(self, message: str) -> tuple[bool, str]:
        return message in self.response.text, (f"Expected message to contain '{message}', "
                                               + f"got {self.response.text}")
