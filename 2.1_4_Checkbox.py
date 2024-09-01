from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    #  Находим значение х для выражения
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    # Находим поле для ввода ответа на выражение и вводим ответ
    input_exp = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_exp.send_keys(y)

    #Отметим checkbox "I'm the robot"
    robotCheck = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robotCheck.click()

    #Выберем radiobutton "Robots rule!".
    robotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robotsRule.click()

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
