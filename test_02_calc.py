from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(browser, 50)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    screen_text = browser.find_element(By.CSS_SELECTOR, ".screen").text
    assert screen_text == "15"