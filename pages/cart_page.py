"""
Page Object para la página del carrito de SauceDemo.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Página del carrito de compras."""

    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")

    def is_cart_page(self):
        """Verifica que estamos en la página del carrito."""
        return "cart" in self.get_current_url()

    def get_cart_items_count(self):
        """Número de ítems en el carrito."""
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def click_checkout(self):
        """Hace clic en Checkout."""
        self.wait_for_clickable(*self.CHECKOUT_BUTTON).click()

    def click_continue_shopping(self):
        """Vuelve a la tienda."""
        self.wait_for_clickable(*self.CONTINUE_SHOPPING).click()
