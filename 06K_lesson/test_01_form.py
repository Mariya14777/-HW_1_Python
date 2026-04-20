from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_form_submission(browser):
    # Открыть страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнить форму
    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    browser.find_element(By.NAME, "zip-code").clear()
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")

    # Скролл до кнопки Submit
    submit_button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    actions = ActionChains(browser)
    actions.move_to_element(submit_button).perform()

    # Нажать Submit
    submit_button.click()

    # Ожидание появления подсветки полей
    wait = WebDriverWait(browser, 10)

    # Проверка: поле Zip code подсвечено красным (alert-danger)
    zip_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_field.get_attribute("class")

    # Проверка: остальные поля подсвечены зеленым (success)
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in fields:
        field = browser.find_element(By.ID, field_id)
        assert "success" in field.get_attribute(
            "class"), f"Field {field_id} is not green"
