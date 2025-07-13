import requests
from requests_toolbelt import MultipartEncoder
import allure
from data import BASE_URL, UPDATE_ORDER_URL


class UpdateOrder:
    @allure.step("Сохраняем для объекта url ручки, токен, headers и обновленный payload")
    def __init__(self, auth_token, order_id, new_name):
        self.url = BASE_URL + UPDATE_ORDER_URL + str(order_id)
        self.auth_token = auth_token
        self.payload = MultipartEncoder(fields={
            "price": "0",
            "name": new_name,
            "category": "Авто",
            "condition": "Новый",
            "city": "Москва",
            "description": "",
            "img1": None,
            "img2": None,
            "img3": None
        })
        self.headers = {"Authorization": self.auth_token, "Content-Type": self.payload.content_type}

    @allure.step("отправляем patch-запрос на изменение данных")
    def change_order(self):
        response = requests.patch(url=self.url, data=self.payload, headers=self.headers)
        return response.status_code, response.json()
