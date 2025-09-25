from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time
import pytest

email = str(time.time()) + "@fakemail.org"

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYea"
        client = LoginPage(browser, link)
        client.open()
        client.go_to_login_page()
        client.register_new_user(email=str(time.time()) + "@fakemail.org", password="19741974r")
        client.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """Открываем страницу товара. Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'  # Stub
        client = ProductPage(browser, url=link)
        client.open()
        assert client.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Присутсвует элемент, которого не должно быть"

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'  # Stub
        # link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'  # Stub

        client = ProductPage(browser, url=link)
        client.open()

        client.is_right_url(), "Проверка на наличие необходимого параметра в ссылке"

        product_cost = client.product_cost()  # Стоимость продукта
        product_name = client.product_name()  # Product name
        time.sleep(5)
        client.add_product_to_basket()  # Добавить продукт в корзину

        client.solve_quiz_and_get_code()

        total_basket_cost = client.total_basket_cost()  # Стоимость всех продуктов в корзине
        product_name_in_basket = client.product_name_in_basket()  # Product name in basket

        try:
            assert product_cost == total_basket_cost and product_name == product_name_in_basket
        except AssertionError:
            raise AssertionError("Product's name or cost difference between basket's cost or name"
                                 f"\nExpected {product_name}, got {product_name_in_basket}, "
                                 f"\nExpected {product_cost}, got {total_basket_cost}"
                                 f"\n Failt link: {link}")

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'  # Stub
    # link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'  # Stub

    client = ProductPage(browser, url=link)
    client.open()

    client.is_right_url(), "Проверка на наличие необходимого параметра в ссылке"

    product_cost = client.product_cost()  # Стоимость продукта
    product_name = client.product_name()  # Product name
    time.sleep(5)
    client.add_product_to_basket()  # Добавить продукт в корзину

    client.solve_quiz_and_get_code()

    total_basket_cost = client.total_basket_cost()  # Стоимость всех продуктов в корзине
    product_name_in_basket = client.product_name_in_basket()  # Product name in basket

    try:
        assert product_cost == total_basket_cost and product_name == product_name_in_basket
    except AssertionError:
        raise AssertionError("Product's name or cost difference between basket's cost or name"
                             f"\nExpected {product_name}, got {product_name_in_basket}, "
                             f"\nExpected {product_cost}, got {total_basket_cost}"
                             f"\n Failt link: {link}")

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """ Гость открывает страницу товара. Переходит в корзину по кнопке в шапке
        Ожидаем, что в корзине нет товаров. Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    client = BasketPage(browser, link)
    client.open()
    client.go_to_basket_page()

    client.is_basket_empty()
    client.is_empty_basket_warnin_exist()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    client = ProductPage(browser, link)
    client.open()
    client.should_be_login_link()
    client.go_to_login_page()

@pytest.mark.xfail(reason='Потому-что надо было брат')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Открываем страницу товара. Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'  # Stub
    client = ProductPage(browser, url=link, timeout=15)
    client.open()
    client.add_product_to_basket()
    client.solve_quiz_and_get_code()
    assert client.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Присутсвует элемент, которого не должно быть"

@pytest.mark.xfail(reason='Потому-что надо было брат')
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Открываем страницу товара. Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""

    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'  # Stub
    client = ProductPage(browser, url=link, timeout=15)
    client.open()
    client.add_product_to_basket()
    client.solve_quiz_and_get_code()
    assert client.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Не исчезло сообщение об успешном добавлении товара в корзину по истечению времени"

# @pytest.mark.skip()
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
