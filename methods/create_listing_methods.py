from requests_toolbelt import MultipartEncoder
import allure
from data import BASE_URL, CREATE_LISTING_URL
import requests

class CreateListingMethods:
    @allure.step("Сохраняем для объекта url и auth_token")
    def __init__(self, auth_token):
        self.url = BASE_URL + CREATE_LISTING_URL
        self.auth_token = "Bearer " + auth_token

    @allure.step("создаем объявление с указанной категорией")
    def create_new_listing(self, listing_category):
        m = MultipartEncoder(fields= {
            "name": "",
            "category": listing_category,
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "0"
        })

        headers = {"Authorization": self.auth_token,
                   "Content-Type": m.content_type
                   }
        response = requests.post(headers= headers, url= self.url, data=m)
        return response.status_code, response.json()

