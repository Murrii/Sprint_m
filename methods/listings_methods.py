import allure
import requests
from data import BASE_URL, DELETE_ORDER_URL


class ListingsMethods:
    @allure.step("Сохраняем url ручки и headers")
    def __init__(self, auth_token, order_id):
        self.url = BASE_URL + DELETE_ORDER_URL + str(order_id)
        self.auth_token = auth_token
        self.headers = {"Authorization": self.auth_token}

    @allure.step("Отправляем delete-запрос")
    def delete_order(self):
        response = requests.delete(url=self.url, headers=self.headers)
        return response.status_code, response.json()
