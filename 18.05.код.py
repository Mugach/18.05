from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Firefox()

try:
    driver.get("https://github.com/login")

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username_input.send_keys("testuser")
    password_input.send_keys("password123")

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='commit']")))
    login_button.click()

    # Ждем, пока загрузится страница профиля пользователя
    profile_page = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@class='avatar avatar-user']")))

    # Создаем скриншот страницы профиля
    driver.save_screenshot("profile_screenshot.png")

except (NoSuchElementException, TimeoutException) as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()