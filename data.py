# urls

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/api/"
REGISTER_URL = "signup"
AUTH_URL = "signin"
CREATE_LISTING_URL = "create-listing"
UPDATE_ORDER_URL = "update-offer/"
DELETE_ORDER_URL = "listings/"

# errors text
ERROR_REGISTER_NOT_UNIQUE_EMAIL = "Почта уже используется"
ERROR_EDIT_ORDER_WIHTOUT_AUTH = "Оффер не найден или у вас нет прав на его редактирование"

# data for auth
AUTH_DATA = {"email": "ktrof_001@mail.ru", "password": "ktrof_001@mail.ru"}
AUTH_DATA_SECOND_USER = {"email": "ktrof_002@mail.ru", "password": "ktrof_002@mail.ru"}

# list of categories
CATEGORIES = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]

# successful order delete text
SUCCESSFUL_ORDER_DELETE_TEXT = "Объявление удалено успешно"