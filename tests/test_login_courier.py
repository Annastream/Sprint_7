import requests
import pytest
import allure
import generators
from data import ResponseBody, Url, DataForAuthorization

class TestLoginCourier:
    @allure.title('Успешная авторизация с логином и паролем. Эндпоинт: /api/v1/courier/login')
    def test_successful_courier_login(self,create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Авторизация под несуществующим пользователем. Эндпоинт: /api/v1/courier/login')
    def test_unregistered_courier_login(self):
        login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_data)
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)


    @allure.title('Регистрация курьера: отсутствует логин или пароль. Эндпоинт: /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForAuthorization.auth_data)
    def test_creation_courier_data_error(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)

