import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(3)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, 'first-name').send_keys('Иван')
    driver.find_element(By.NAME, 'last-name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'zip-code').send_keys('')
    driver.find_element(By.NAME, 'city').send_keys('Москва')
    driver.find_element(By.NAME, 'country').send_keys('Россия')
    driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, 'job-position').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')
    driver.find_element(By.CLASS_NAME, 'btn-outline-primary').click()


    field_zip = driver.find_element(
        By.ID, 'zip-code').get_attribute('class')
    assert field_zip == 'alert py-2 alert-danger'

    field_first_name = driver.find_element(
        By.ID, 'first-name').get_attribute('class')
    assert field_first_name == 'alert py-2 alert-success'

    field_last_name = driver.find_element(
        By.ID, 'last-name').get_attribute('class')
    assert field_last_name == 'alert py-2 alert-success'

    field_address = driver.find_element(
        By.ID, 'address').get_attribute('class')
    assert field_address == 'alert py-2 alert-success'

    field_city = driver.find_element(
        By.ID, 'city').get_attribute('class')
    assert field_city == 'alert py-2 alert-success'

    field_country = driver.find_element(
        By.ID, 'country').get_attribute('class')
    assert field_country == 'alert py-2 alert-success'

    field_mail = driver.find_element(
        By.ID, 'e-mail').get_attribute('class')
    assert field_mail == 'alert py-2 alert-success'

    field_phone = driver.find_element(
        By.ID, 'phone').get_attribute('class')
    assert field_phone == 'alert py-2 alert-success'

    field_company = driver.find_element(
        By.ID, 'company').get_attribute('class')
    assert field_company == 'alert py-2 alert-success'
    driver.quit()
