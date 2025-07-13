from requests_toolbelt import MultipartEncoder
import allure
from data import BASE_URL, CREATE_LISTING_URL
import requests

class CreateListingMethods:
    @allure.step("Сохраняем для объекта url ручки, auth_token, payload и headers")
    def __init__(self, auth_token, order_category):
        self.url = BASE_URL + CREATE_LISTING_URL
        self.auth_token = auth_token
        self.payload = MultipartEncoder(fields= {
            "name": "",
            "category": order_category,
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "price": "0"
        })
        self.headers = {"Authorization": self.auth_token,
                   "Content-Type": self.payload.content_type
                   }

    @allure.step("создаем объявление с указанной категорией")
    def create_new_order(self):
        response = requests.post(headers= self.headers, url= self.url, data=self.payload)
        return response.status_code, response.json()

    @allure.step("Создаем объявление и возвращаем его id")
    def get_new_order_id(self):
        _, json = self.create_new_order()
        return json["id"]
