from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("12345")
    print("Введено: 12345")
    time.sleep(1)

    input_field.clear()
    print("Поле очищено")
    time.sleep(1)

    input_field.send_keys("54321")
    print("Введено: 54321")

finally:
    time.sleep(1)
    driver.quit()
