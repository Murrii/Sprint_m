from methods.register_methods import RegisterMethods
from data import ERROR_REGISTER_NOT_UNIQUE_EMAIL
import allure


class TestRegister:
    @allure.title("Регистрация пользователя с уникальным email")
    def test_register_new_user_with_unique_email_status_code_201(self, email_generator):
        register = RegisterMethods(email_generator)
        status_code, json = register.register_new_user()
        assert status_code == 201 and json["user"]["email"] == email_generator

    @allure.title("Регистрация пользователя с не уникальным email")
    def test_register_new_user_with_not_unique_email_status_code_400(self, email_generator):
        register = RegisterMethods(email_generator)
        register.register_new_user()
        status_code, json = register.register_new_user()
        assert status_code == 400 and json["message"] == ERROR_REGISTER_NOT_UNIQUE_EMAIL
