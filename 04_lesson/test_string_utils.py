import pytest
from string_utils import StringUtils

# Создаем экземпляр класса для использования в тестах
utils = StringUtils()

# ==================== Тесты для метода capitalize ====================


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("s", "S"),                     # Один символ
    ("тест", "Тест"),               # Русские буквы
])
def test_capitalize_positive(input_str, expected):
    """Позитивные тесты: первая буква становится заглавной"""
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),            # Начинается с цифры
    ("", ""),                        # Пустая строка
    ("   ", "   "),                  # Только пробелы
    ("SKYPRO", "Skypro"),            # Все заглавные
    ("sKyPrO", "Skypro"),            # Перемешанный регистр
])
def test_capitalize_negative(input_str, expected):
    """Негативные тесты: граничные случаи для capitalize"""
    assert utils.capitalize(input_str) == expected


# ==================== Тесты для метода trim ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("hello", "hello"),
    ("   hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты: удаление пробелов в начале строки"""
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                         # Пустая строка
    ("   ", ""),                      # Только пробелы
    ("skypro   ", "skypro   "),       # Пробелы в конце не удаляются
    ("   skypro   ", "skypro   "),    # Пробелы в начале и конце
])
def test_trim_negative(input_str, expected):
    """Негативные тесты: граничные случаи для trim"""
    assert utils.trim(input_str) == expected


# ==================== Тесты для метода contains ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),      # Символ в начале
    ("SkyPro", "o", True),      # Символ в конце
    ("SkyPro", "k", True),      # Символ в середине
    ("SkyPro", "Pro", True),    # Подстрока
    ("abc", "", True),          # Пустой символ (согласно реализации)
])
def test_contains_positive(string, symbol, expected):
    """Позитивные тесты: символ или подстрока найдены"""
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),      # Символ не найден
    ("", "a", False),            # Пустая строка
    (" ", " ", True),            # Пробел как символ
    ("abc", "z", False),         # Символ отсутствует
])
def test_contains_negative(string, symbol, expected):
    """Негативные тесты: символ или подстрока не найдены"""
    assert utils.contains(string, symbol) == expected


# ==================== Тесты для метода delete_symbol ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # Удаление символа
    ("SkyPro", "Pro", "Sky"),      # Удаление подстроки
    ("aaaaa", "a", ""),            # Удаление всех символов
    ("abcabc", "b", "acac"),       # Удаление повторяющихся
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные тесты: символ или подстрока удалены"""
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),                 # Пустая строка
    ("SkyPro", "", "SkyPro"),      # Пустой символ для удаления
    ("abc", "z", "abc"),           # Символ не найден
    (" ", " ", ""),                # Пробел
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные тесты: граничные случаи для delete_symbol"""
    assert utils.delete_symbol(string, symbol) == expected


# ==================== Дополнительные тесты (по желанию) ====================

def test_with_none_values():
    """Тесты на передачу None (ожидаем исключения)"""
    with pytest.raises(AttributeError):
        utils.capitalize(None)

    with pytest.raises(AttributeError):
        utils.trim(None)

    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
