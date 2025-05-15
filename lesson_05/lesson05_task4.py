from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

input_user = driver.find_element(By.CSS_SELECTOR, "#username")
input_user.send_keys("tomsmith")

input_pass = driver.find_element(By.CSS_SELECTOR, "#password")
input_pass.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
sleep(5)

success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(success_message.text)

driver.quit()
