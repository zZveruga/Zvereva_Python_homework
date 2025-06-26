import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity(allure.severity_level.MINOR)
class Calculator:
    """
    Представляет страницу калькулятора.
    """

    def __init__(self, driver):
        """
        Конструктор класса.
        """
        self.driver = driver
        # Открываем страницу калькулятора
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Нажатие кнопки {button}")
    def click_buttons(self, button: str) -> None:
        """
        Нажимает указанную кнопку на странице калькулятора.
        """
        element = self.driver.find_element(By.XPATH, f"//span[text()='{button}']")
        element.click()

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay: float) -> None:
        """
        Устанавливает задержку отображения результата вычисления.
        """
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(str(delay))

    @allure.step("Получение результата расчета")
    def get_result(self, result: str, delay: float) -> int:
        """
        Получает результат вычислений после заданной задержки.
        """
        locator = (By.XPATH, f"//div[text()='{result}']")
        wait = WebDriverWait(self.driver, delay + 1, poll_frequency=1)
        result_element = wait.until(EC.visibility_of_element_located(locator))
        result_value = int(result_element.text)
        return result_value
