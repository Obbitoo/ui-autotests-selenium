from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    COST_OF_BOOK = (By.XPATH, '//tr[3]/td[1]')
    TOTAL_COST_OF_BASKET = (By.XPATH, '//div[3]/div/p/strong[1]')
    PRODUCT_NAME = (By.XPATH, '//h1[1]')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, """//strong[text()="The shellcoder's handbook"]""")

if __name__ == '__main__':
    ...