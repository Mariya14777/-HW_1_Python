from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    # Ждем появления текста "Done!" (все картинки загружены)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    # Находим картинки только в контейнере
    selector = "#image-container img"
    images = driver.find_elements(By.CSS_SELECTOR, selector)

    print(f"Найдено картинок в контейнере: {len(images)}")

    # Выводим src третьей картинки (индекс 2)
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("Загружено меньше 3-х картинок")

finally:
    driver.quit()
