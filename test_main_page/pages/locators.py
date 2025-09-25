from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    ENTER_WITH_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_WITH_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_WITH_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_WITH_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_WITH_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    COST_OF_BOOK = (By.XPATH, '//tr[3]/td[1]')
    TOTAL_COST_OF_BASKET = (By.XPATH, '//div[3]/div/p/strong[1]')
    PRODUCT_NAME = (By.XPATH, '//h1[1]')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasketPageLocators:
    GO_TO_BASKET_PAGE = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '.page-header')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs > div > h2')

if __name__ == '__main__':
    ...