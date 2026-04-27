from services.yougile_api import ProjectsAPI


class TestProjectsAPI:
    """Тесты для API проектов Yougile"""

    # ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_success(self, projects_api):
        """Позитивный тест: создание проекта с валидными данными"""
        project_title = "New Test Project"

        response = projects_api.create_project(project_title)

        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        response_data = response.json()
        assert "id" in response_data, "Response should contain 'id' field"
        assert response_data.get("title") == project_title, "Project title mismatch"

        project_id = response_data.get("id")
        if project_id:
            projects_api.delete_project(project_id)

    def test_get_project_success(self, projects_api, test_project_id):
        """Позитивный тест: получение проекта по ID"""
        response = projects_api.get_project(test_project_id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        response_data = response.json()
        assert response_data.get("id") == test_project_id, "Project ID mismatch"
        assert "title" in response_data, "Response should contain 'title' field"

    def test_update_project_success(self, projects_api, test_project_id):
        """Позитивный тест: обновление проекта"""
        new_title = "Updated Project Title"

        response = projects_api.update_project(test_project_id, title=new_title)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        get_response = projects_api.get_project(test_project_id)
        assert get_response.json().get("title") == new_title, "Project title was not updated"

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_empty_title(self, projects_api):
        """Негативный тест: создание проекта с пустым названием"""
        response = projects_api.create_project("")

        assert response.status_code in [400, 422], \
            f"Expected error status (400/422), got {response.status_code}"

        response_data = response.json()
        assert "error" in response_data or "message" in response_data, \
            "Response should contain error message"

    def test_create_project_missing_title(self, projects_api):
        """Негативный тест: создание проекта без обязательного поля title"""
        response = projects_api._request("POST", "/projects", data={})

        assert response.status_code in [400, 422], \
            f"Expected error status (400/422), got {response.status_code}"

    def test_get_nonexistent_project(self, projects_api):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"

        response = projects_api.get_project(fake_id)

        assert response.status_code == 404, \
            f"Expected 404, got {response.status_code}"

        response_data = response.json()
        assert "error" in response_data or "message" in response_data, \
            "Response should contain error message"

    def test_update_nonexistent_project(self, projects_api):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"

        response = projects_api.update_project(fake_id, title="New Title")

        assert response.status_code in [404, 400], \
            f"Expected error status (404/400), got {response.status_code}"

    def test_update_project_invalid_data(self, projects_api, test_project_id):
        """Негативный тест: обновление проекта с некорректными данными"""
        response = projects_api.update_project(test_project_id, title=12345)

        assert response.status_code in [400, 422], \
            f"Expected error status (400/422), got {response.status_code}"

    def test_create_project_without_auth(self):
        """Негативный тест: создание проекта без авторизации"""
        api = ProjectsAPI()
        api.headers = {"Content-Type": "application/json"}

        response = api.create_project("Test Without Auth")

        assert response.status_code in [401, 403], \
            f"Expected auth error (401/403), got {response.status_code}"
