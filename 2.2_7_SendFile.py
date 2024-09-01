from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import os


link = 'https://suninjuly.github.io/file_input.html'

try:
    fake = Faker()
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    fname = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys(fake.first_name())
    lname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys(fake.last_name())
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(fake.email())

 
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)


    
    submitbtn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    


finally:
    time.sleep(5)
    browser.quit()