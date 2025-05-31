import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


@pytest.mark.usefixtures()
def test():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    expectation = driver.find_element(By.ID, "delay")
    expectation.clear()
    expectation.send_keys("10")
    driver.find_element(By.XPATH, "//span[text()= '7']").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//span[text()= '+']").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//span[text()= '8']").click()
    WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//span[text()= '=']").click()
    result_log = (By.XPATH, "//div[text()= '15']")
    result_1 = WebDriverWait(driver, 11, 1).until(
        EC.visibility_of_element_located(result_log))
    result = int(result_1.text)
    assert result == 15
    driver.quit()
