from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(edge_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

wait = WebDriverWait(driver, 10)


wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#langSelect-EN'))).click()
cookie = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#bigCookie')))
for i in range(10):
    cookie.click()
