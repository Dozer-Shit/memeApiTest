import allure
import requests

from typing import Any

from meme_api_tests.endpoints.schemas import ResponseSchema
from meme_api_tests.utils.client import attach_error


class BaseApi:
    meme_id: str
    response_json: dict
    response: requests.Response
    valid_response: ResponseSchema
    token: str

    @allure.step('Validate response schema')
    def validate_response(self, schema: Any) -> None:
        try:
            self.valid_response = schema(**self.response.json())
        except Exception as e:
            attach_error(str(e), name="Validation Error")
            assert False, f"Validation error: {str(e)}"

    @allure.step('Check status code')
    def check_status_code_is_(self, status_code: int) -> None:
        assert self.response.status_code == status_code, (
            f"Expected status code {status_code}, got {self.response.status_code}"
        )

    @allure.step('Check response text')
    def check_response_text_is_(self, text_resp: str) -> None:
        assert self.valid_response.text == text_resp, (f"Expected name {text_resp}, "
                                                       + f"got {self.valid_response.text}")

    @allure.step('Check response url')
    def check_response_url_is_(self, url_resp: str) -> None:
        assert self.valid_response.url == url_resp, (f"Expected year {url_resp}, "
                                                     + f"got {self.valid_response.url}")

    @allure.step('Check response tags')
    def check_response_tags_is_(self, tags_resp: list) -> None:
        assert self.valid_response.tags == tags_resp, (f"Expected hard disk size {tags_resp}, "
                                                       + f"got {self.valid_response.tags}")

    @allure.step('Check response message')
    def check_response_message_is_(self, message: str) -> None:
        assert message in self.response.text, (
            f"Expected message to contain '{message}', got {self.response.text}"
        )
