import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.severity(allure.severity_level.BLOCKER)
class ShoppingCartPage:
    """
    Класс описывает взаимодействие с страницей корзины покупок.
    """

    def __init__(self, driver):
        """
        Инициализация класса и открытие главной страницы магазина.
        """
        self.driver = driver
        self.waiter = WebDriverWait(driver, 40)
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Войти с логином {username} и паролем {password}")
    def login(self, username, password):
        """
        Выполняет авторизацию на сайте.
        :param username: Логин пользователя
        :param password: Пароль пользователя
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @allure.step("Добавить товар с id={product_id} в корзину")
    def add_product_to_cart(self, product_id):
        """
        Добавляет выбранный товар в корзину.
        :param product_id: Идентификатор товара
        """
        product_locator = (By.ID, f"add-to-cart-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(product_locator)
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Перейти на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step("Перешли к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Продолжить процесс оформления заказа.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    @allure.step("Заполнить контактные данные: имя={first_name}, фамилия={last_name}, почтовый индекс={postal_code}")
    def fill_checkout_form(self, first_name, last_name, postal_code):
        """
        Заполняет контактную информацию на этапе оформления заказа.
        :param first_name: Имя покупателя
        :param last_name: Фамилия покупателя
        :param postal_code: Почтовый индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    @allure.step("Получить общую стоимость заказа")
    def get_total_price(self) -> str:
        """
        Возвращает итоговую сумму заказа.
        :return: Общая стоимость заказа (строка)
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
