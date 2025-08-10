#from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(4)

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    #sleep(2)

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    #sleep(2)

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    #sleep(2)

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Юлия')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Ерисова')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('443028')

    #sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
    #sleep(2)

    total_text = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    total = total_text.replace('Total: ', '')

    print(total)
    #sleep(20)
    #driver.quit()

    assert total == '$58.29'