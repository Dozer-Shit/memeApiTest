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

    def validate_response(self, schema: Any) -> None:
        schema_name = schema.__name__
        with allure.step(f'Validate response schema: {schema_name}'):
            try:
                self.valid_response = schema(**self.response.json())
                allure.attach(str(self.valid_response), name="Validated Response",
                              attachment_type=allure.attachment_type.JSON)
            except Exception as e:
                attach_error(str(e), name="Validation Error")
                assert False, f"Validation error: {str(e)}"

    @allure.step('Check status code')
    def check_status_code_is_(self, status_code: int) -> None:
        assert self.response.status_code == status_code, (
            f"Expected status code is {status_code}, got this {self.response.status_code}"
        )

    @allure.step('Check response text')
    def check_response_text_is_(self, text_resp: str) -> None:
        assert self.valid_response.text == text_resp, (f"Expected name is {text_resp}, "
                                                       + f"got this {self.valid_response.text}")

    @allure.step('Check response url')
    def check_response_url_is_(self, url_resp: str) -> None:
        assert self.valid_response.url == url_resp, (f"Expected year is {url_resp}, "
                                                     + f"got this {self.valid_response.url}")

    @allure.step('Check response tags')
    def check_response_tags_is_(self, tags_resp: list) -> None:
        assert self.valid_response.tags == tags_resp, (f"Expected tags is {tags_resp}, "
                                                       + f"got this {self.valid_response.tags}")

    @allure.step('Check response info')
    def check_response_info_is_(self, info_resp: list) -> None:
        assert self.valid_response.info == info_resp, (f"Expected info is {info_resp}, "
                                                       + f"got this {self.valid_response.tags}")

    @allure.step('Check response message')
    def check_response_message_is_(self, message: str) -> None:
        assert message in self.response.text, (
            f"Expected message to contain string '{message}', got this {self.response.text}"
        )
