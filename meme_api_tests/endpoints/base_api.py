import allure
import requests

from meme_api_tests.endpoints.schemas import ResponseSchema


class BaseApi:
    meme_id: str
    response_json: dict
    response: requests.Response
    valid_response: ResponseSchema
    token: str

    @allure.step('Check status code')
    def check_status_code_is_(self, status_code: int) -> tuple[bool, str]:
        return self.response.status_code == status_code, (f"Expected status code {status_code}, "
                                                          + f"got {self.response.status_code}")

    @allure.step('Check response text')
    def check_response_text_is_(self, text_resp: str) -> tuple[bool, str]:
        return self.valid_response.text == text_resp, (f"Expected name {text_resp}, "
                                                       + f"got {self.valid_response.text}")

    @allure.step('Check response url')
    def check_response_url_is_(self, url_resp: str) -> tuple[bool, str]:
        return self.valid_response.url == url_resp, (f"Expected year {url_resp}, "
                                                     + f"got {self.valid_response.url}")

    @allure.step('Check response type')
    def check_response_type_is_(self, type_resp: str) -> tuple[bool, str]:
        return self.valid_response.info.type == type_resp, (f"Expected price {type_resp}, "
                                                            + f"got {self.valid_response.info.type}")

    @allure.step('Check response title')
    def check_response_title_is_(self, title_resp: str) -> tuple[bool, str]:
        return self.valid_response.info.title == title_resp, (f"Expected cpu model {title_resp}, "
                                                              + f"got {self.valid_response.info.title}")

    @allure.step('Check response tags')
    def check_response_hard_disk_size_is_(self, tags_resp: list) -> tuple[bool, str]:
        return self.valid_response.tags == tags_resp, (f"Expected hard disk size {tags_resp}, "
                                                       + f"got {self.valid_response.tags}")

    @allure.step('Check response message')
    def check_response_message_is_(self, message: str) -> tuple[bool, str]:
        return message in self.response.text, (f"Expected message to contain '{message}', "
                                               + f"got {self.response.text}")
