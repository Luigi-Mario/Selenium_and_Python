from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    submitbtn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    new_window = browser.window_handles[1] # Получаем имя новой вкладки
    browser.switch_to.window(new_window) # Переключаемся на новую вкладку

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(int(x))
    answer = browser.find_element(By.ID, 'answer').send_keys(str(res))
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
   time.sleep(5)
   browser.quit()