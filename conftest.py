import pytest
import allure
import random
from methods.auth_methods import AuthMethods


@allure.title("генерируем строку для регистрации")
@pytest.fixture
def email_generator():
    random_number_string = str(random.randint(1000, 9999))
    generated_email = "ktrof_" + random_number_string + "@mail.ru"
    return generated_email

@allure.title("авторизируемся и возвращаем токен")
@pytest.fixture
def get_auth_token():
    method = AuthMethods()
    _, json = method.auth_user()
    return json["token"]["access_token"]
