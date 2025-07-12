from methods.create_listing_methods import CreateListingMethods
import pytest
import allure
from data import CATEGORIES


class TestCreateListing:
    @allure.title("Создаем объявления всех возможных категорий (параметризация)")
    @pytest.mark.parametrize("category", CATEGORIES)
    def test_create_new_listing_with_all_categories_successful_status_code_201(self, get_auth_token, category):
        method = CreateListingMethods(get_auth_token)
        status_code, json = method.create_new_listing(category)
        assert status_code == 201 and json["category"] == category, print(json)
