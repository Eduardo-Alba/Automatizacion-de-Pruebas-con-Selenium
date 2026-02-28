"""
Page Object para la página de productos (inventory) de SauceDemo.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    """Página de listado de productos."""

    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU = (By.CLASS_NAME, "bm-menu")

    def is_products_page(self):
        """Verifica que estamos en la página de productos."""
        return "inventory" in self.get_current_url()

    def get_page_title(self):
        """Obtiene el título de la página."""
        elem = self.wait_for_element(*self.TITLE)
        return elem.text

    def get_product_count(self):
        """Devuelve el número de productos visibles."""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)

    def add_first_product_to_cart(self):
        """Añade el primer producto al carrito."""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if buttons:
            self.wait_for_clickable(*self.ADD_TO_CART_BUTTON)
            buttons[0].click()

    def add_product_by_index(self, index):
        """Añade el producto en el índice dado al carrito (0-based)."""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if index < len(buttons):
            buttons[index].click()

    def get_cart_count(self):
        """Devuelve el número del badge del carrito, o 0 si no hay."""
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self):
        """Navega al carrito."""
        self.wait_for_clickable(*self.CART_LINK).click()

    def logout(self):
        """Abre el menú y cierra sesión."""
        self.wait_for_clickable(*self.MENU_BUTTON).click()
        # Esperar a que el menú sea visible para evitar race conditions con la animación
        self.wait_for_element(*self.MENU)
        self.wait_for_clickable(*self.LOGOUT_LINK).click()

    def sort_by(self, value):
        """Ordena por el valor dado (e.g. 'lohi', 'hilo', 'az', 'za')."""
        from selenium.webdriver.support.ui import Select
        dropdown = self.wait_for_element(*self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(value)
