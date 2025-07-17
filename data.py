
import generators

class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/' # Url Yandex Scooter
    CREATE_COURIER = '/api/v1/courier' # Создание курьера
    COURIER_LOGIN = '/api/v1/courier/login' # Логин курьера в системе
    MAKE_ORDER = '/api/v1/orders'  # Создание заказа
    GET_ORDER_LIST = '/api/v1/orders' # Получение списка заказов
    ORDER_CANCEL = '/api/v1/orders/cancel' # Отменить заказ
    TRACK_ORDER = '/api/v1/orders/track?t=' # Получить заказ по его номеру
    COURIER_DELETE = '/api/v1/courier/:id' # Удаление курьера

class DataForOrder:
    order_data = {
        "firstName": "Foxxy",
        "lastName": "Toshibba",
        "address": "Scramble, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class DataForRegistration:
    reg_data = [
        {'password': generators.password_generator(), 'firstName': generators.name_generator()},  # No login
        {'login': generators.login_generator(), 'firstName': generators.name_generator()}  # No password
    ]

class DataForAuthorization:
    auth_data = [
        {'password': generators.password_generator()},  # No login
        {'login': generators.login_generator()}  # No password
    ]

class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, "message": "Этот логин уже используется. Попробуйте другой."}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, "message": "Недостаточно данных для создания учетной записи"}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, "message": "Учетная запись не найдена"}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, "message": "Недостаточно данных для создания учетной записи"}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track' # Успешное создание заказа
    SUCCESSFUL_GET_ORDER_LIST = 'orders' # Успешное получение списка заказов
