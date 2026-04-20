from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    # Ждем загрузки минимум 3 картинок
    wait = WebDriverWait(driver, 30)
    wait.until(lambda d: len(d.find_elements(
        By.CSS_SELECTOR, "#image-container img")) >= 3)

    # Находим все картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("Загружено меньше 3-х картинок")

finally:
    driver.quit()
