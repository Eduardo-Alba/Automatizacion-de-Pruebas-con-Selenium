"""
Casos de prueba: Carrito de compras (añadir producto, badge, navegación).
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import config


class TestCart:
    """Pruebas del carrito."""

    def test_anadir_producto_al_carrito(self, logged_in_driver, products_page):
        """
        Caso de prueba: Añadir un producto al carrito.
        Pasos: Login, clic en "Add to cart" del primer producto.
        Resultado esperado: Badge del carrito muestra 1.
        """
        products_page.add_first_product_to_cart()
        assert products_page.get_cart_count() == 1

    def test_anadir_varios_productos(self, logged_in_driver, products_page):
        """
        Caso de prueba: Añadir dos productos; el badge debe reflejar la cantidad.
        """
        products_page.add_product_by_index(0)
        products_page.add_product_by_index(1)
        assert products_page.get_cart_count() >= 2

    def test_ir_al_carrito_y_ver_productos(self, logged_in_driver, products_page, cart_page):
        """
        Caso de prueba: Añadir producto, ir al carrito y verificar ítems.
        """
        products_page.add_first_product_to_cart()
        products_page.go_to_cart()
        assert cart_page.get_cart_items_count() >= 1
