from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from math import log, sin

link = "https://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(log(abs(12 * sin(x)))))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    alert = WebDriverWait(browser, timeout=5).until(lambda doc : doc.switch_to.alert)
    print(alert.text)
    alert.accept()