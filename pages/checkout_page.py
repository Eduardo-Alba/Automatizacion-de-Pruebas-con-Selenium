"""
Page Object para el flujo de checkout de SauceDemo.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Página de información de checkout (Step One)."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    TITLE = (By.CLASS_NAME, "title")

    def fill_info(self, first_name, last_name, postal_code):
        """Rellena el formulario de checkout."""
        self.wait_for_element(*self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element(*self.LAST_NAME).send_keys(last_name)
        self.wait_for_element(*self.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        """Continúa al resumen del pedido."""
        self.wait_for_clickable(*self.CONTINUE_BUTTON).click()


class CheckoutOverviewPage(BasePage):
    """Página de resumen del pedido (Step Two)."""

    TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")

    def click_finish(self):
        """Finaliza el pedido."""
        self.wait_for_clickable(*self.FINISH_BUTTON).click()


class CheckoutCompletePage(BasePage):
    """Página de pedido completado."""

    TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")

    def get_complete_message(self):
        """Obtiene el mensaje de éxito."""
        elem = self.wait_for_element(*self.COMPLETE_HEADER)
        return elem.text

    def is_order_complete(self):
        """Verifica que estemos en la página de pedido completado (URL o mensaje)."""
        url = self.get_current_url()
        if "checkout-complete" in url:
            return True
        try:
            # Esperar mensaje de éxito (puede haber redirección lenta)
            msg = self.get_complete_message()
            return bool(msg and "thank" in msg.lower())
        except Exception:
            return False
