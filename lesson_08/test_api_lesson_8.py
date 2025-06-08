import pytest
import requests


url = 'https://yougile.com'
projects = '/api-v2/projects'
auth = {"Authorization": "Bearer DkGIr1X0jC4Y1khGc5A07y27Y1DUPVU-iHu-Uv8-Bugq-XQKVAZH0CqpAx0mwPWY"}


@pytest.fixture()
def create_project():
    body = {
        'title': 'Домашка 8'
    }
    response = requests.post(url + projects, json=body, headers=auth)
    assert response.status_code == 201
    return response.json()['id']


class TestProjectsAPI:

    def test_project_post_positive(self, create_project):
        #создание нового проекта
        body = {
            'title': 'Домашка 8.0'
        }
        response = requests.post(url + projects, json=body, headers=auth)
        assert response.status_code == 201
        body = response.json()
        assert body['id']


    def test_project_post_negative(self):
        #отсутствие обязательного поля title при создании проекта
        body = {}
        response = requests.post(url + projects, json=body, headers=auth)
        assert response.status_code == 400

        expected_response_body = {
            "statusCode": 400,
            "message": [
                "title should not be empty",
                "title must be a string"
            ],
            "error": "Bad Request"
        }

        actual_response_body = response.json()
        assert actual_response_body == expected_response_body


    def test_project_put_positive(self, create_project):
        #обновление существующего проекта
        body = {
            'title': 'Домашка 8, update'
        }
        response = requests.put(f"{url}{projects}/{create_project}", json=body, headers=auth)
        assert response.status_code == 200
        body = response.json()
        assert body['id']


    def test_project_put_negative(self, create_project):
        #попытка обновить несуществующий проект
        project_id = 'not_exist-id'
        body = {
            'title': 'Домашка 8, update'
        }
        response = requests.put(f"{url}{projects}/{project_id}", json=body, headers=auth)
        assert response.status_code == 404


    def test_project_get_positive(self, create_project):
        #получение информации о существующем проекте
        response = requests.get(f"{url}{projects}/{create_project}", headers=auth)
        assert response.status_code == 200
        body = response.json()
        assert body['title'] == 'Домашка 8'


    def test_project_get_negative(self):
        #попытка получить несуществующий проект
        project_id = 'not_exist-id'
        response = requests.get(f"{url}{projects}/{project_id}", headers=auth)

        expected_response_body ={
            "statusCode": 404,
            "message": "Проект не найден",
            "error": "Not Found"
        }
        actual_response_body = response.json()
        assert actual_response_body == expected_response_body
