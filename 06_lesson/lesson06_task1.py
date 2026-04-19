from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем на синюю кнопку
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    button.click()

    # Ждем появления зеленой плашки с текстом
    success_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    print(success_message.text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
