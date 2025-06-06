from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def click_buttons(self, button):
        self.driver.find_element(By.XPATH, f"//span[text()= '{button}']").click()

    def set_delay(self, delay):
        expectation = self.driver.find_element(By.ID, "delay")
        expectation.clear()
        expectation.send_keys(f"{delay}")

    def get_result(self, result, delay):
        result_log = (By.XPATH, f"//div[text()= '{result}']")
        result_1 = WebDriverWait(self.driver, delay+1, 1).until(
            EC.visibility_of_element_located(result_log))
        result2 = int(result_1.text)
        return result2
