from .pages.product_page import ProductPage



def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    client = ProductPage(browser, link)
    client.open()

    client.is_right_url(), "Отсутствует необходимый параметр в ссылке"
    product_cost = client.product_cost()  # Стоимость продукта
    product_name = client.product_name()  # Product name
    client.add_product_to_basket()  # Добавить продукт в корзину
    client.solve_quiz_and_get_code()
    total_basket_cost = client.total_basket_cost()  # Стоимость всех продуктов в корзине
    product_name_in_basket = client.product_name_in_basket()  # Product name in basket

    try:
        assert product_cost == total_basket_cost and product_name == product_name_in_basket
    except AssertionError:
        raise AssertionError("Product's name or cost difference between basket's cost or name")
