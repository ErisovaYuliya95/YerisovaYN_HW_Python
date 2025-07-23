from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")
search_locator = 'input'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys('Sky')
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys('Pro')
sleep(2)

driver.quit()
