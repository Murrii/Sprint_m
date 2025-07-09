import pytest
import allure
import random

@allure.title("генерируем строку для регистрации")
@pytest.fixture
def email_generator():
    random_number_string = str(random.randint(1000, 9999))
    generated_email = "ktrof_" + random_number_string + "@mail.ru"
    return generated_email