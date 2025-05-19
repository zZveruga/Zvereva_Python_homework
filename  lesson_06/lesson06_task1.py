from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.implicitly_wait(11)
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
txt = driver.find_element(
    By.CLASS_NAME, "bg-success").text

print(txt)


driver.quit()
