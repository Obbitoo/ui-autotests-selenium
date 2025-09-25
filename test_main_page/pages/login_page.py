from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.go_to_login_page()
        self.should_be_login_link()
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_WITH_LOGIN)
        register_email_field.send_keys(self.email)

        register_password_first = self.browser.find_element(*LoginPageLocators.REGISTER_WITH_PASSWORD)
        register_password_first.send_keys(self.password)

        register_password_second = self.browser.find_element(*LoginPageLocators.REGISTER_WITH_PASSWORD_REPEAT)
        register_password_second.send_keys(self.password)

        register_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_BUTTON)
        register_confirm.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link_text = self.browser.current_url
        assert "login" in link_text, "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.presense_of_element_and_click(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.presense_of_element_and_click(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"
