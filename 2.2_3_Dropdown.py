from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    num1 = browser.find_element(By.ID, 'num1')
    num1 = int(num1.text)
    num2 = browser.find_element(By.ID, 'num2')
    num2 = int(num2.text)
    result = num1 + num2

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    submitbtn = browser.find_element(By.XPATH, ("//button[text()='Submit']")).click()
    
finally:
    time.sleep(5)
    browser.quit()

