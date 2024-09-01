from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    # Ищем элемент и получаем скрытый аттрибут
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    # Ищем поле для ввода и вводим значение полученное после вычисления функции calc
    x = calc(x)
    input_x = browser.find_element(By.ID, 'answer')
    input_x.send_keys(x)
    # Отмечаем checkbox "I'm the robot"
    robotCheck = browser.find_element(By.ID, 'robotCheckbox')
    robotCheck.click()
    # Отмечаем radiobutton "Robots rule!".
    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()
    # Находим кнопку Submit и подтверждаем отправку формы
    submitbtn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    submitbtn.click()
    

finally:
    time.sleep(10)
    browser.quit()
    
