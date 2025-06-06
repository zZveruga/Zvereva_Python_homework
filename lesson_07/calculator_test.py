from selenium import webdriver
from calculator import Calculator


def test():
    driver = webdriver.Chrome()
    calculator = Calculator(driver)
    delay = 45
    calculator.set_delay(delay)

    calculator.click_buttons('7')
    calculator.click_buttons('+')
    calculator.click_buttons('8')
    calculator.click_buttons('=')

    assert calculator.get_result(15, delay) == 15
    driver.quit()