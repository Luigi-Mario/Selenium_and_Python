from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'https://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    good_price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button_price = browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(int(x))

    answer = browser.find_element(By.ID, 'answer').send_keys(str(res))
    submitbtn = browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(20)
    browser.quit()