import allure
from methods.listings_methods import ListingsMethods
from data import SUCCESSFUL_ORDER_DELETE_TEXT


class TestListing:
    @allure.title("Удаление объявления под токеном создателя объявления")
    def test_delete_order_created_by_auth_user_status_code_200(self, get_auth_token_and_order_id):
        token, order_id = get_auth_token_and_order_id
        method = ListingsMethods(token, order_id)
        status_code, json = method.delete_order()
        assert status_code == 200 and json["message"] == SUCCESSFUL_ORDER_DELETE_TEXT
