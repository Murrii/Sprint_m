import requests
import allure

from data import BASE_URL, REGISTER_URL

class RegisterMethods:
    @allure.step("генерируем адрес ручки регистрации и данные для запроса для дальнейшей работы")
    def __init__(self, email_string):
        self.url = BASE_URL + REGISTER_URL
        self.payload = {"email": email_string,
                        "password": email_string,
                        "submitPassword": email_string}

    @allure.step("отправляем POST-запрос на регистрацию со сгенерированными при создании объекта данными")
    def register_new_user(self):
        response = requests.post(url = self.url, data = self.payload)
        return response.status_code, response.json()
