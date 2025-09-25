from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def is_right_url(self):
        link_text = self.browser.current_url
        # Hard-coded parameter Promo
        assert '?promo=newYear' in link_text, f'Parameter "?promo=newYear" absence, got {link_text}'

    def add_product_to_basket(self):
        assert self.presense_of_element_and_click(*ProductPageLocators.ADD_PRODUCT_TO_BASKET, press=True)

    def product_cost(self):
        return self.element_text(*ProductPageLocators.COST_OF_BOOK)

    def total_basket_cost(self):
        return self.element_text(*ProductPageLocators.TOTAL_COST_OF_BASKET)

    def product_name(self):
        return self.element_text(*ProductPageLocators.PRODUCT_NAME)

    def product_name_in_basket(self):
        return self.element_text(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"