import allure
import requests

from meme_api_tests.client import MEME_URL

from meme_api_tests.endpoints.base_api import BaseApi


class DeleteMeme(BaseApi):
    @allure.step('Delete meme object')
    def delete_meme_object(self, meme_id: int, token: str) -> None:
        headers = {"Authorization": token}
        self.response: requests.Response = requests.delete(f"{MEME_URL}/{meme_id}", headers=headers)
        print(self.response.status_code)
        print(self.response.text)
