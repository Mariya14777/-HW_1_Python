from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    # Ждем загрузки картинки
    wait = WebDriverWait(driver, 30)
    wait.until(EC.visibility_of_element_located((By.ID, "landscape")))

    src = driver.find_element(By.ID, "landscape").get_attribute("src")
    print(src)

finally:
    driver.quit()
