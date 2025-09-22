from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from math import sin, log

class BasePage():

    def __init__(self, browser, url, timeout=10):
        """Создание объекта веб клиента"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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
