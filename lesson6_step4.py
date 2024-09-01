from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    fname = browser.find_element(By.CSS_SELECTOR, "[placeholder*='first']")
    fname.send_keys("Ivan")
    lname = browser.find_element(By.CSS_SELECTOR, "[placeholder*='last']")
    lname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder*='email']")
    email.send_keys("ip@mail.nnov")
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder*='phone']")
    phone.send_keys("+1555353555")
    adress = browser.find_element(By.CSS_SELECTOR, "[placeholder*='address']")
    adress.send_keys("New York, st. AllahuAcbar, 1, 1")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


