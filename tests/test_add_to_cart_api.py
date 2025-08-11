import pytest
import requests
import allure
from models.api_add_to_cart_model import AddToCartResponse


@allure.title('Тест API добавления товара в корзину')
@pytest.mark.parametrize('product_id, price, quantity', [
    (966, '4 900', 1),
    (927, '12 200', 2),
    (925, '14 400', 3)
])

def test_add_to_cart_api(product_id, price, quantity):
    cart_url = 'https://m-g-p.ru/cart/add/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://m-g-p.ru/',
    }
    payload = {
        'product_id':product_id,
        'quantity':quantity,
        'html':True
    }
    session = requests.Session()

    with allure.step('Отправляем Post-запрос на сервер'):
        response = session.post(cart_url, data=payload, headers=headers)

    with allure.step('Валидация ответа через Pydantic'):
        try:
            api_obj = AddToCartResponse.model_validate(response.json())
        except Exception as e:
            pytest.fail(f'Ошибка валидации: {e}')

    with allure.step('Проверяем содержимое ответа'):
        assert response.status_code == 200
        assert price in api_obj.data.total
        assert quantity == api_obj.data.count

