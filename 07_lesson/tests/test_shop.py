from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_checkout(browser):
    login_page = LoginPage(browser)
    login_page.open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items:
        inventory_page.add_item_to_cart(item)
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_form("Иван", "Петров", "123456")
    total = checkout_page.get_total()

    assert total == "58.29", f"Expected $58.29, but got ${total}"
