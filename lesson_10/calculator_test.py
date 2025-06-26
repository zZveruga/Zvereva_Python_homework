import pytest
import allure
from selenium import webdriver
from calculator import Calculator


@pytest.fixture(scope="module")
def browser():
    """Фикстура для запуска браузера."""
    with webdriver.Chrome() as driver:
        yield driver
        driver.quit()


@allure.title("Проверка правильности сложения чисел")
@allure.description("Тест проверяет правильное выполнение операции сложения.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(browser):
    """
    Тест проверяет правильность сложения чисел на калькуляторе.
    """
    calculator = Calculator(browser)
    delay = 45
    calculator.set_delay(delay)

    with allure.step("Ввод первого числа"):
        calculator.click_buttons('7')

    with allure.step("Выбор оператора '+'"):
        calculator.click_buttons('+')

    with allure.step("Ввод второго числа"):
        calculator.click_buttons('8')

    with allure.step("Выполнение операции '='"):
        calculator.click_buttons('=')

    with allure.step("Проверка результата вычисления"):
        actual_result = calculator.get_result('15', delay)
        assert actual_result == 15, f"Ожидалось значение 15, получено {actual_result}"
