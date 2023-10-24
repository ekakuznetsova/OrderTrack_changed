import configuration
import data
import requests
import pytest
 #Выполняем запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL+configuration.CREATE_ORDER_PATH,
                         json=body)
#Получаем номер трека
def get_track():
    response = post_new_order(data.order_body)
    track = response.json()["track"]; #Записываем номер трека в переменную track
    return track

#Функция для подстановки номера трека в URL
def get_order_by_track():
    track = get_track()
    link = {'t': track} #Создаем словарь для подстановки номера трека в URL
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH, params=link)

