from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator(browser):
    # Открыть страницу
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввести задержку 45 секунд
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать кнопки: 7 + 8 =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата (таймаут 50 секунд, т.к. задержка 45 секунд)
    wait = WebDriverWait(browser, 50)
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))

    # Проверка результата
    screen_text = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert screen_text == "15"
