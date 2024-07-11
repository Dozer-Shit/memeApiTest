import os
import allure

from pathlib import Path

from typing import Any

from dotenv import load_dotenv, set_key

load_dotenv()

BASE_URL: str = os.getenv('BASE_URL')
MEME_URL: str = os.getenv('MEME_URL')
AUTHORIZE_URL: str = os.getenv('AUTHORIZE_URL')
AUTHORIZATION_TOKEN: str = os.getenv('AUTHORIZATION_TOKEN')

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / '.env'


def save_token(token: str) -> None:
    set_key(ENV_FILE, "AUTHORIZATION_TOKEN", token)


def attach_response(response: dict, name: str) -> allure:
    allure.attach(str(response), name=name, attachment_type=allure.attachment_type.JSON)


def attach_error(value: str, name: str) -> allure:
    allure.attach(value, name=name, attachment_type=allure.attachment_type.TEXT)


def allure_annotations(title: str, story: str, description: str, tag: str = "",
                       severity: allure = allure.severity_level.NORMAL, feature: str = "MEME API") -> Any:
    def wrapper(func: Any) -> Any:
        func = allure.title(title)(func)
        func = allure.feature(feature)(func)
        func = allure.story(story)(func)
        func = allure.severity(severity)(func)
        func = allure.description(description)(func)
        func = allure.tag(tag)(func)
        return func

    return wrapper


def validate_response(self, response_json: dict, response_type: str, schema: Any) -> Any:
    if 'Bad Request' in response_json:
        attach_error(str(response_json), name="Invalid Response")
        assert False, "Response does not contain necessary fields"
    else:
        try:
            valid_response = schema(**response_json)
            if response_type == "Response":
                self.valid_response = valid_response
                return self.valid_response
            elif response_type == "TokenGetResponse":
                self.valid_response = valid_response
                return self.valid_response
        except Exception as e:
            attach_error(str(e), name="Validation Error")
            assert False, f"Validation error: {str(e)}"
