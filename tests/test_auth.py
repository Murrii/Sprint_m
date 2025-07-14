from methods.auth_methods import AuthMethods
from data import AUTH_DATA
import allure


class TestAuth:
    @allure.title("Успешная регистрация заранее зарегистрированного пользователя")
    def test_auth_user_with_valid_data_status_code_201(self):
        method = AuthMethods()
        status_code, json = method.auth_user()
        assert status_code == 201 and json["user"]["email"] == AUTH_DATA["email"]
