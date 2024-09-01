from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    #Находим значение х и расчитываем ответ в функции calc
    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)

    #Вводим ответ в поле для ответа
    answer = browser.find_element(By.ID, 'answer').send_keys(str(res))
    #Отмечаем чекбокс и прокручиваем до радиобаттона и отмечаем его
    robotcheckbox = browser.find_element(By.ID, 'robotCheckbox').click()
    robotsrule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsrule)
    robotsrule.click()

    #Прокручиваем до скрытой кнопки Submit и отправлем форму
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(5)
    browser.quit()