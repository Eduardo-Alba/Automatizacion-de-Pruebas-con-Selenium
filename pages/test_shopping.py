import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, CheckoutOverviewPage, CheckoutCompletePage

@pytest.fixture
def logged_in_driver(driver):
    """Fixture auxiliar que devuelve un driver ya logueado."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    return driver

def test_add_product_to_cart(logged_in_driver):
    """Verifica que se pueda añadir un producto al carrito."""
    products_page = ProductsPage(logged_in_driver)
    
    # Añadir primer producto
    products_page.add_first_product_to_cart()
    
    # Verificar badge del carrito
    assert products_page.get_cart_count() == 1, "El contador del carrito debería mostrar 1."

def test_complete_checkout_flow(logged_in_driver):
    """
    Escenario End-to-End:
    1. Añadir producto al carrito.
    2. Ir al carrito y hacer checkout.
    3. Llenar información de envío.
    4. Finalizar orden.
    5. Verificar mensaje de éxito.
    """
    # 1. Añadir producto
    products_page = ProductsPage(logged_in_driver)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    
    # 2. Verificar carrito y proceder
    cart_page = CartPage(logged_in_driver)
    assert cart_page.is_cart_page()
    cart_page.click_checkout()
    
    # 3. Información de Checkout
    checkout_page = CheckoutPage(logged_in_driver)
    checkout_page.fill_info("Test", "User", "12345")
    checkout_page.click_continue()
    
    # 4. Resumen y Finalizar
    overview_page = CheckoutOverviewPage(logged_in_driver)
    overview_page.click_finish()
    
    # 5. Confirmación
    complete_page = CheckoutCompletePage(logged_in_driver)
    assert complete_page.is_order_complete(), "La orden no se completó exitosamente."