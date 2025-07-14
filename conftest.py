import pytest
import allure
import random
from methods.auth_methods import AuthMethods
from data import AUTH_DATA
from methods.create_listing_methods import CreateListingMethods


@allure.title("Генерируем строку для регистрации")
@pytest.fixture
def email_generator():
    random_number_string = str(random.randint(1000, 9999))
    generated_email = "ktrof_" + random_number_string + "@mail.ru"
    return generated_email

@allure.title("Авторизируемся и возвращаем токен")
@pytest.fixture
def get_auth_token():
    method = AuthMethods()
    return method.get_token_auth_user(AUTH_DATA)


@allure.title("Авторизируемся, создаем объявление, возвращаем токен и id объявления")
@pytest.fixture
def get_auth_token_and_order_id(get_auth_token):
    method = CreateListingMethods(auth_token=get_auth_token, order_category="Авто")
    order_id = method.get_new_order_id()
    return get_auth_token, order_id
