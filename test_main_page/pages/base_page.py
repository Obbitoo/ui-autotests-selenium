from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators
from .locators import BasePageLocators
from math import sin, log

class BasePage:

    def __init__(self, browser, url, timeout=10):
        """Создание объекта веб клиента"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.GO_TO_BASKET_PAGE)
        link.click()

    def should_be_login_link(self):
        assert self.presense_of_element_and_click(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_exist(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def open(self):
        """Открывает указанную страницу в браузера"""
        self.browser.get(self.url)

    def presense_of_element_and_click(self, how, what, press=False):
        """Булевый сёрчер по заданному методу поиска и клик кнопки если пресс True"""
        try:
            element = self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

        else:
            if press:
                element.click()
            return True

    def element_text(self, how, what):
        """Булевый сёрчер по заданному методу поиска и клик кнопки если пресс True"""
        try:
            element = self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

        else:
            return element.text

    def is_not_element_present(self, how, what, timeout=4):
        """is_not_element_present: упадет, как только увидит искомый элемент. Не появился: успех, тест green"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """будет ждать до тех пор, пока элемент не исчезнет"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_exist(self, how, what, timeout=4):
        """будет ждать до тех пор, пока элемент не исчезнет"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        """Для получения кода"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
