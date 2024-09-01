from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    alert = browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(int(x))

    answer = browser.find_element(By.ID, 'answer').send_keys(str(res))
    submitbtn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
   time.sleep(3)
   browser.quit()
