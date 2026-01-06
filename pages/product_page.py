# product_page.py
# =====================
# This class represents the "Product Page" of the application.
# It follows the Page Object Model (POM) pattern to separate
# locators (web elements) and actions (user interactions)
# from the test logic for better reusability and maintenance.

from playwright.sync_api import Page, expect
from pages.shopping_cart_page import ShoppingCartPage  # Adjust path as per your folder structure


class ProductPage:
    """Page Object Model class for the Product Page."""

    def __init__(self, page: Page):
        """
        Constructor to initialize the Playwright Page instance
        and define all the locators used on the Product Page.
        """
        self.page = page

        # ===== Locators =====
        # Using CSS selectors to identify page elements
        self.txt_quantity = page.locator('input[name="quantity"]')
        self.btn_add_to_cart = page.locator('#button-cart')
        self.cnf_msg = page.locator('.alert.alert-success.alert-dismissible')
        self.btn_items = page.locator('#cart')
        self.lnk_view_cart = page.locator('strong:has-text("View Cart")')

    # ===== Quantity Methods =====

    def set_quantity(self, qty: str):
        """
        Set the desired product quantity before adding to cart.
        Clears the existing value and enters the new quantity.
        """
        try:
            self.txt_quantity.fill('')   # Clear existing value
            self.txt_quantity.fill(qty)  # Enter new quantity
        except Exception as e:
            print(f"Error while setting quantity: {e}")
            raise

    # ===== Add to Cart Methods =====

    def add_to_cart(self):
        """
        Click the 'Add to Cart' button to add the selected product.
        """
        try:
            self.btn_add_to_cart.click()
        except Exception as e:
            print(f"Error while clicking 'Add to Cart': {e}")
            raise

    # ===== Confirmation Message =====

    def get_confirmation_message(self):
        """
        Return the confirmation message element shown after adding to cart.
        Useful for validating success notifications.

        Example:
            expect(product_page.get_confirmation_message()).to_be_visible()
        """
        try:
            return self.cnf_msg
        except Exception as e:
            print(f"Confirmation message not found: {e}")
            return None

    # ===== Navigate to Shopping Cart =====

    def click_items_to_navigate_to_cart(self):
        """
        Click the cart icon (usually at the top-right corner)
        to open the cart dropdown or popup.
        """
        try:
            self.btn_items.click()
        except Exception as e:
            print(f"Error while clicking cart items button: {e}")
            raise

    def click_view_cart(self) -> ShoppingCartPage:
        """
        Click the 'View Cart' link inside the cart dropdown.
        Returns an instance of the ShoppingCartPage class.

        Example:
            shopping_cart_page = product_page.click_view_cart()
        """
        try:
            self.lnk_view_cart.click()
            return ShoppingCartPage(self.page)
        except Exception as e:
            print(f"Error while clicking 'View Cart': {e}")
            raise

    # ===== Combined Workflow =====

    def add_product_to_cart(self, quantity: str):
        """
        Combined workflow to:
        1. Set product quantity
        2. Add product to the cart
        3. Validate confirmation message (optional)
        """
        try:
            self.set_quantity(quantity)
            self.add_to_cart()
            expect(self.get_confirmation_message()).to_be_visible()
        except Exception as e:
            print(f"Error in add_product_to_cart workflow: {e}")
            raise
