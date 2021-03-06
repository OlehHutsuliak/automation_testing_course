from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    # line below will  check is it the right page
    product_page.should_be_url_attribute()
    product_page.add_product_to_basket()
    product_page.check_product_in_message()
