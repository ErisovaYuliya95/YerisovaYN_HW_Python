import requests
import pytest

base_url = 'https://ru.yougile.com/api-v2/'
token  = '' #необходимо получить/создать свой ключ и указать в переменную
project_id = '' #необходимо указать id проекта в переменной
not_id = '2f243d08-9e89-4c0f-9b17-8ef60219209' # неверный Id



#1. создание проекта
#позитивная проверка
@pytest.mark.positive
def test_create_project_positive():
    my_project = {
        "title": "Домашка №8"
    }
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.post(base_url + 'projects', headers=my_headers, json=my_project)
    assert resp.status_code == 201

@pytest.mark.negative
def test_create_project_negative():
    my_project = {
        "title": ""
    }
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.post(base_url + 'projects', headers=my_headers, json=my_project)
    assert resp.status_code == 400


#2. получение данных о проекте по id
@pytest.mark.positive
def test_get_project_positive():
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + 'projects/' + project_id, headers=my_headers)
    title = resp.json()["title"]
    assert resp.status_code == 200
    assert title == "Тестовый проект"

@pytest.mark.negative
def test_get_project_negative():
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + 'projects/' + not_id, headers=my_headers)
    message = resp.json()["message"]
    assert message == "Проект не найден"
    assert resp.status_code == 404


#3. изменение данных проекта по id
@pytest.mark.positive
def test_change_project_positive():
    my_project = {
        "title": "Скайпро1"
    }
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    before_id = requests.post(base_url + 'projects', headers=my_headers, json=my_project).json()["id"]

    new_project = {
        "title": "Скайпро2"
    }
    resp = requests.put(base_url + 'projects/' + before_id, headers=my_headers, json=new_project)
    after_id = resp.json()["id"]
    assert resp.status_code == 200
    assert after_id == before_id

@pytest.mark.negative
def test_change_project_negative():
    my_project = {
        "title": "Скаенг1"
    }
    my_headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    before_id = requests.post(base_url + 'projects', headers=my_headers, json=my_project).json()["id"]

    new_project = {
        "title": ""
    }
    resp = requests.put(base_url + 'projects/' + before_id, headers=my_headers, json=new_project)
    message = resp.json()["message"]
    assert message == ['title should not be empty']
    assert resp.status_code == 400
