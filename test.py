import configuration
import data
import requests
import pytest
import sender_stand_request

#Кузнецова Екатерина, 9 когорта, финальный проект

# Проверяем, что код ответа 200
def response_code_assert():
    response = sender_stand_request.get_order_by_track()
    assert response.status_code == 200

# Тест 1. Проверка получения кода 200 на запрос на получение заказа по трек-номеру
def test_get_order_by_track():
    response_code_assert()

