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
response = requests.request("POST", url, data=payload)

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
    with open("../post_users.json") as file:
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

# Эта функция тестирует, возвращает ли сервер уникальных пользователей при запросе.
#
# Отправка GET-запроса: Метод requests.get используется для отправки GET-запроса
# на URL "https://reqres.in/api/users" с параметрами page (страница 2) и per_page (4 пользователя).
# Параметр verify=False отключает проверку SSL-сертификатов, что может быть полезно в тестовых средах, хотя не рекомендуется на продакшене.
#
# Получение идентификаторов пользователей:
#
# В ответе извлекается JSON-данные, и собираются идентификаторы пользователей из поля data в переменную ids.
# Проверка уникальности идентификаторов:
#
# Сравнивается длина списка ids с длиной множества, созданного из ids.
# Множество автоматически удаляет дубликаты, поэтому, если длины совпадают, значит,
# все идентификаторы уникальны.
# Таким образом, эта функция проверяет, что пользователи, возвращаемые на второй
# странице, являются уникальными. Если длина списка идентификаторов равна длине множества,
# значит, в ответе нет дубликатов.


def test_get_users_returns_unique_users():
    response = requests.get(
        url="https://reqres.in/api/users",
        params={"page": 2, "per_page": 4},
        verify=False
    )
    ids = [element["id"] for element in response.json()["data"]]

    assert len(ids) == len(set(ids))

