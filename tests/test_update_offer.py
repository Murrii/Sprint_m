import allure
from methods.update_offer_methods import UpdateOrder
from methods.auth_methods import AuthMethods
from data import AUTH_DATA_SECOND_USER, ERROR_EDIT_ORDER_WIHTOUT_AUTH


class TestUpdateOrder:
    @allure.title("Редактирование объявления под токеном создателя объявления")
    def test_update_order_created_by_auth_user_status_code_200(self, get_auth_token_and_order_id, email_generator):
        token, order_id = get_auth_token_and_order_id
        method = UpdateOrder(token, order_id, email_generator)
        status_code, json = method.change_order()
        assert status_code == 200 and json["name"] == email_generator, print(json)

    @allure.title("Редактирование объявления под чужим токеном")
    def test_update_order_not_created_by_auth_user_status_code_401(self,get_auth_token_and_order_id, email_generator):
        _, order_id = get_auth_token_and_order_id
        second_user_auth_method = AuthMethods()
        second_user_token = second_user_auth_method.get_token_auth_user(AUTH_DATA_SECOND_USER)
        update_order_method = UpdateOrder(auth_token=second_user_token, order_id=order_id, new_name=email_generator)
        status_code, json = update_order_method.change_order()
        assert status_code == 401 and json["message"] == ERROR_EDIT_ORDER_WIHTOUT_AUTH
