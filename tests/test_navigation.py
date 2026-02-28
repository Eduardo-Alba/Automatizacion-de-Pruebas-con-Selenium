"""
Casos de prueba: Navegación y funcionalidad de la página de productos.
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import config


@pytest.mark.smoke
class TestNavigation:
    """Pruebas de navegación entre secciones."""

    def test_ir_al_carrito_desde_productos(self, logged_in_driver, products_page):
        """
        Caso de prueba: Navegar al carrito desde la página de productos.
        Precondición: Usuario logueado en /inventory.
        Pasos: Clic en icono del carrito.
        Resultado esperado: URL contiene 'cart', página del carrito visible.
        """
        cart_page = CartPage(logged_in_driver)
        products_page.go_to_cart()
        assert cart_page.is_cart_page(), "Debe estar en la página del carrito"

    def test_continuar_comprando_desde_carrito(self, logged_in_driver, products_page, cart_page):
        """
        Caso de prueba: Desde el carrito, volver a la tienda.
        Precondición: Usuario en /cart.
        Pasos: Añadir un producto, ir al carrito, Continuar comprando.
        Resultado esperado: Volver a /inventory.
        """
        products_page.add_first_product_to_cart()
        products_page.go_to_cart()
        cart_page.click_continue_shopping()
        assert products_page.is_products_page()

    def test_cerrar_sesion(self, logged_in_driver, login_page, products_page):
        """
        Caso de prueba: Cerrar sesión desde el menú.
        Pasos: Abrir menú, Logout.
        Resultado esperado: Volver a la página de login.
        """
        products_page.logout()
        # Verificar que estamos en la página de login (URL base o formulario visible)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(logged_in_driver, 15)
        wait.until(lambda d: config.BASE_URL in d.current_url or "inventory" not in d.current_url)
        assert config.BASE_URL in logged_in_driver.current_url or login_page.is_login_visible()
