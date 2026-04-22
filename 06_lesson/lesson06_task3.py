from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    wait = WebDriverWait(driver, 30)

    # Ждем загрузки третьей картинки (award)
    third_image = wait.until(
        lambda d: d.find_element(By.ID, "award")
        if d.find_element(By.ID, "award").get_attribute("src")
        else False
    )

    print(third_image.get_attribute("src"))

finally:
    driver.quit()
