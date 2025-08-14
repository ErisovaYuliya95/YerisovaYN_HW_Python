from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self._driver = driver

    # указать время загрузки результата
    def send_time(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    # жмякаем по кнопкам калькулятора
    def calculate(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    # получаем результат подсчета
    def get_result(self):
        WebDriverWait(self._driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text