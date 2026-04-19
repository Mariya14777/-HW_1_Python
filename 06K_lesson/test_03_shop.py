from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout(browser):
    # Открыть сайт магазина
    browser.get("https://www.saucedemo.com/")

    # Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Ожидание загрузки страницы
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "inventory_item")))

    # Добавление товаров в корзину
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items:
        item = browser.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        item.click()

    # Перейти в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажать Checkout
    browser.find_element(By.ID, "checkout").click()

    # Заполнить форму данными
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")

    # Нажать Continue
    browser.find_element(By.ID, "continue").click()

    # Ожидание загрузки итоговой страницы
    wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))

    # Прочитать итоговую стоимость
    total_text = browser.find_element(
        By.CLASS_NAME, "summary_total_label").text
    total_value = total_text.replace("Total: $", "")

    # Проверка итоговой суммы
    assert total_value == "58.29", f"Expected $58.29, but got ${total_value}"
