import pytest
import allure
from selenium import webdriver
from shopping_cart_page import ShoppingCartPage


@pytest.fixture
def driver():
    """
    Фикстура для запуска веб-драйвера.
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@allure.title("Проверка функционала корзины покупок")
@allure.description("Тестирует полный цикл работы с корзиной покупок.")
@allure.feature("Корзина покупок")
@allure.story("Добавление товаров, переход к оформлению заказа и проверка общей стоимости")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart(driver):
    """
    Проверяет полную последовательность операций с корзиной покупок:
     - Вход на сайт
     - Добавление продуктов в корзину
     - Оформление заказа
     - Проверка итоговой суммы
    """
    page = ShoppingCartPage(driver)
    page.login("standard_user", "secret_sauce")

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    for product_id in products:
        page.add_product_to_cart(product_id)

    page.go_to_cart()
    page.proceed_to_checkout()
    page.fill_checkout_form("Татьяна", "Зверева", "115533")

    assert page.get_total_price() == "Total: $58.29"
