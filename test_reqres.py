import json

import requests
from jsonschema import validate

url = "https://reqres.in/api/users"
# Задается url ,на который будет отправлен POST-запрос,
# и создается полезная нагрузка (payload),
# содержащая имя (name) и должность (job).
payload = {"name": "morpheus", "job": "leader"}
# Отправка POST-запроса: Используется метод requests.request
# для отправки POST-запроса с полезной нагрузкой. Результат запроса выводится на экран
response = requests.("POST", url, data=payload)

print(response.text)


# Функция test_schema_validate_from_file:
#
# Отправляет POST-запрос с данными о пользователе ("morpheus", "master").
# Проверяет, что статус код ответа равен 201 (что означает успешное создание).
# Загружает JSON-схему из файла post_users.json и проверяет,
# соответствует ли полученный ответ этой схеме с помощью функции validate.
def test_schema_validate_from_file():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
    body = response.json()

    assert response.status_code == 201

    # Валидация схемы: Открывается файл с именем "post_users.json" для чтения,
    # и его содержимое интерпретируется как JSON-объект.
    # Затем осуществляется валидация body (ответа) с этим JSON-объектом
    # с использованием функции validate.
    with open("post_users.json") as file:
        validate(body, schema=json.loads(file.read()))

# Эта функция тестирует,
# возвращается ли правильная информация о пользователе
# после отправки запроса на создание пользователя.
# Отправка POST-запроса: Используется метод requests.post для отправки
# POST-запроса на URL "https://reqres.in/api/users" с данными в формате JSON.
# Данные содержат ранее указанные name и job.
# Получение ответа: Содержимое ответа сохраняется в переменной body, преобразуется в формат JSON.

def test_job_name_from_request_returns_in_response():
    job = "master"
    name = "morpheus"

    response = requests.post("https://reqres.in/api/users", json={"name": name, "job": job})
    body = response.json()

    assert body["name"] == name
    assert body["job"] == job

