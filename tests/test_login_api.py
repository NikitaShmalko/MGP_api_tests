import pytest
import requests
import allure
from models.api_login_model import LoginResponse


@allure.title('Тест API логина')

def test_login_api():
    login_url = 'https://m-g-p.ru/login/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://m-g-p.ru/',
    }

    payload = {
        'login':'shmalkopress@gmail.com',
        'password':'test_password',
        'wa_auth_login':1,
        'wa_json_mode':1,
        'need_redirects':1
    }

    session = requests.Session()

    with allure.step('Отправляем Post-запрос на сервер'):
        response = session.post(login_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):
        try:
            api_obj = LoginResponse.model_validate(response.json())
        except Exception as e:
             pytest.fail(f'Ошибка валидации ответа API: {e}')

    with allure.step('Проверяем содержимое ответа'):
        assert api_obj.status == 'ok'
        assert response.status_code == 200
        assert api_obj.data.redirect_url is not None









