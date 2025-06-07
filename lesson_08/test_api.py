import pytest
import requests


url = 'https://yougile.com'
projects = '/api-v2/projects'
auth = {'Authorization': 'DkGIr1X0jC4Y1khGc5A07y27Y1DUPVU-iHu-Uv8-Bugq-XQKVAZH0CqpAx0mwPWY'}


@pytest.fixture(scope='module')
def create_project():
    #Фикстура для создания проекта перед началом тестирования
    payload = {
        'title': 'Домашка 8'
    }
    response = requests.post(url + projects, json=payload, headers=auth)
    assert response.status_code == 201
    return response.json()['id']


class TestProjectsAPI:

    def test_create_project_post_positive(self):
        #Тестирование успешного создания нового проекта
        payload = {
            'title': 'Домашка 8.0'
        }
        response = requests.post(url + projects, json=payload, headers=auth)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == 'Домашка 8.0'


    def test_create_project_post_negative_missing_name(self):
        #Негативный сценарий — отсутствие обязательного поля title
        payload = {}
        response = requests.post(url + projects, json=payload, headers=auth)
        assert response.status_code in [400, 401, 422]
        error_data = response.json()
        assert 'title' in error_data.get('errors', 'title')


    @pytest.mark.usefixtures("create_project")
    def test_update_project_put_positive(self, create_project):
        #Обновление существующего проекта
        update_payload = {
            'title': 'Домашка 8, update'
        }
        response = requests.put(f"{url}/{projects}/{create_project}", json=update_payload, headers=auth)
        assert response.status_code == 200
        updated_data = response.json()
        assert updated_data['title'] == 'Домашка 8, update'


    @pytest.mark.usefixtures("create_project")
    def test_update_project_put_negative_wrong_id(self, create_project):
        #Попытка обновить несуществующий проект
        wrong_id = 'nonexistent-id'
        update_payload = {
            'title': 'Домашка 8, update'
        }
        response = requests.put(f"{url}/{projects}/{wrong_id}", json=update_payload, headers=auth)
        assert response.status_code in [400, 404]


    @pytest.mark.usefixtures("create_project")
    def test_get_project_get_positive(self, create_project):
        #Получение информации о существующем проекте
        response = requests.get(f"{url}/{projects}/{create_project}", headers=auth)
        assert response.status_code == 200
        project_data = response.json()
        assert project_data['title'] == 'Домашка 8'


    def test_get_project_get_negative_nonexistent_id(self):
        #Попытка получить несуществующий проект
        non_existent_id = 'invalid-project-id'
        response = requests.get(f"{url}/{projects}/{non_existent_id}", headers=auth)
        assert response.status_code == 404
