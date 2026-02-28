"""
Casos de prueba: Flujo de checkout completo.
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, CheckoutOverviewPage, CheckoutCompletePage
import config


@pytest.mark.checkout
class TestCheckout:
    """Pruebas del proceso de checkout."""

    def test_checkout_completo_exitoso(
        self, logged_in_driver, products_page, cart_page
    ):
        """
        Caso de prueba: Login -> Añadir producto -> Carrito -> Checkout -> Datos -> Finish.
        Datos: Nombre, Apellido, Código postal.
        Resultado esperado: Página "Thank you for your order!".
        """
        products_page.add_first_product_to_cart()
        products_page.go_to_cart()
        cart_page.click_checkout()

        checkout_one = CheckoutPage(logged_in_driver)
        checkout_one.fill_info("Juan", "Pérez", "28001")
        checkout_one.click_continue()

        overview = CheckoutOverviewPage(logged_in_driver)
        overview.click_finish()

        complete = CheckoutCompletePage(logged_in_driver)
        msg = complete.get_complete_message()
        assert msg and "thank" in msg.lower(), f"Mensaje de confirmación esperado, obtenido: {msg}"
