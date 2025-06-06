import pytest
from selenium import webdriver
from shop import ShoppingCartPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


def test_shopping_cart(driver):
    page = ShoppingCartPage(driver)

    page.login("standard_user", "secret_sauce")

    for product_id in ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]:
        page.add_product_to_cart(product_id)

    page.go_to_cart()
    page.proceed_to_checkout()
    page.fill_checkout_form("Татьяна", "Зверева", "115533")

    assert page.get_total_price() == "Total: $58.29"