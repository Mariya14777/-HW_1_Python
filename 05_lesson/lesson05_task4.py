from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()

    time.sleep(2)

    success_msg = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print("Сообщение после авторизации:", success_msg.text)

finally:
    time.sleep(1)
    driver.quit()
