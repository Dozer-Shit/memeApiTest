import allure
import requests

from meme_api_tests.client import AUTHORIZE_URL, validate_response

from meme_api_tests.endpoints.base_api import BaseApi

from meme_api_tests.endpoints.schemas import TokenGetResponseSchema


class PostAuthorize(BaseApi):
    @allure.step('Authorize and get token')
    def get_token(self, payload: dict) -> str:
        self.response: requests.Response = requests.post(AUTHORIZE_URL, json=payload)
        response_json: dict = self.response.json()
        valid_response: TokenGetResponseSchema = validate_response(self, response_json,
                                                                   "TokenGetResponse", TokenGetResponseSchema)
        self.token: str = valid_response.token

        return self.token

    @allure.step('Check response name')
    def check_response_name_is_(self, name: str) -> tuple[bool, str]:
        return name in self.valid_response.user, (f"Expected message to contain '{name}', "
                                                  + f"got {self.valid_response.user}")
