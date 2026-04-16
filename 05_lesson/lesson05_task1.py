from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    print("Клик по синей кнопке выполнен успешно!")

finally:
    time.sleep(1)
    driver.quit()
