from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    wait = WebDriverWait(driver, 10)
    inp = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
    inp.send_keys("SkyPro")

    btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    btn.click()

    wait2 = WebDriverWait(driver, 10)
    wait2.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"
        )
    )

    print(btn.text)

finally:
    driver.quit()
