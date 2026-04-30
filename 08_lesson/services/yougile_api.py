import requests
from config import BASE_URL, ENDPOINTS, get_auth_headers


class YougileAPI:
    """Базовый класс для работы с API"""

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = get_auth_headers()

    def _request(self, method, endpoint, data=None, expected_status=None):
        """Универсальный метод для отправки запросов"""
        url = f"{self.base_url}{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=data
        )

        if expected_status and response.status_code != expected_status:
            raise AssertionError(
                f"Expected status {expected_status}, got {response.status_code}. "
                f"Response: {response.text}"
            )

        return response


class ProjectsAPI(YougileAPI):
    """Класс для работы с проектами"""

    def create_project(self, title, **kwargs):
        """Создание проекта POST /api-v2/projects"""
        data = {"title": title}
        data.update(kwargs)
        return self._request("POST", ENDPOINTS["projects"], data=data)

    def update_project(self, project_id, **kwargs):
        """Обновление проекта PUT /api-v2/projects/{id}"""
        endpoint = ENDPOINTS["project"].format(id=project_id)
        return self._request("PUT", endpoint, data=kwargs)

    def get_project(self, project_id):
        """Получение проекта по ID GET /api-v2/projects/{id}"""
        endpoint = ENDPOINTS["project"].format(id=project_id)
        return self._request("GET", endpoint)

    def delete_project(self, project_id):
        """Удаление проекта DELETE /api-v2/projects/{id}"""
        endpoint = ENDPOINTS["project"].format(id=project_id)
        return self._request("DELETE", endpoint)
