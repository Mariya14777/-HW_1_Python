import os


# Базовые настройки API
BASE_URL = "https://httpbin.org"  # Замените на ваш домен
API_VERSION = "v2"


# Эндпоинты
ENDPOINTS = {
    "projects": "/post",
    "project": "/put/{id}"
}


# Заголовки по умолчанию
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def get_api_key():
    """Получить API ключ из переменных окружения"""
    api_key = os.environ.get("YOUGILE_API_KEY", "test-key-123")
    return api_key


def get_auth_headers():
    """Получить заголовки с токеном авторизации"""
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {get_api_key()}"
    return headers
