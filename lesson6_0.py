from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    # Заполняем обязательные поля
    fname = browser.find_element(By.CSS_SELECTOR, ".first_block .first[required]")
    fname.send_keys("Ivan")
    lname = browser.find_element(By.CSS_SELECTOR, ".first_block .second[required]")
    lname.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third[required]")
    email.send_keys("ip@mail.nnov")
    # Заполняем не обязательные поля
    '''
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    phone.send_keys("+1555353555")
    adress = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    adress.send_keys("New York, st. AllahuAcbar, 1, 1")
    '''

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


