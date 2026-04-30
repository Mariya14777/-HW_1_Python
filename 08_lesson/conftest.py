import pytest
from services.yougile_api import ProjectsAPI


@pytest.fixture
def projects_api():
    """Фикстура для работы с API проектов"""
    return ProjectsAPI()


@pytest.fixture
def test_project_id(projects_api):
    """
    Фикстура для создания тестового проекта и его последующего удаления.
    """
    response = projects_api.create_project("Test Project for API Tests")
    assert response.status_code == 201, f"Failed to create test project: {response.text}"

    project_id = response.json().get("id")
    yield project_id

    try:
        projects_api.delete_project(project_id)
    except Exception:
        pass
