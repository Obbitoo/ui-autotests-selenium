from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def is_empty_basket_warnin_exist(self):
        assert self.is_element_exist(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Where is no text with a warning about emptiness of basket"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Where are items in product basket"
