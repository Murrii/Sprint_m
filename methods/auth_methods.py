import allure
import requests
from data import BASE_URL, AUTH_URL,AUTH_DATA


class AuthMethods:
    @allure.step("сохраняем для объекта адрес ручки авторизации и данные для запроса для дальнейшей работы")
    def __init__(self):
        self.url = BASE_URL + AUTH_URL
        self.payload = AUTH_DATA

    @allure.step("авторизируемся в системе")
    def auth_user(self):
        response = requests.post(url=self.url, data=self.payload)
        return response.status_code, response.json()
