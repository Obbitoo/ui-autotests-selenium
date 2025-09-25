from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from time import sleep
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link, 10)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """  Гость открывает главную страницу. Переходит в корзину по кнопке в шапке сайта.
            Ожидаем, что в корзине нет товаров. Ожидаем, что есть текст о том что корзина пуста.
        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        client = BasketPage(browser, link)
        client.open()
        client.go_to_basket_page()

        client.is_basket_empty()
        client.is_empty_basket_warnin_exist()
