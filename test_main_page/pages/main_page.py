from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def go_to_login_page(self):
        """Открыть окно авторизации"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.presense_of_element_and_click(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
