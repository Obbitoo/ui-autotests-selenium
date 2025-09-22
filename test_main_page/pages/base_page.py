from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10):
        """Создание объекта веб клиента"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает указанную страницу в браузера"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Булевый сёрчер по заданному методу поиска"""
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

        else:
            return True
