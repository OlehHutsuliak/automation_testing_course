import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_url_attribute()
        self.should_be_add_to_basket_button()

    def add_product_to_basket(self):
        self.click_on_the_basket()
        self.solve_quiz_and_get_code()

    def check_product_in_message(self):
        self.product_name_in_message()
        self.product_price_in_message()

    # next three functions add product to basket and check the massage after
    def click_on_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_name_in_message(self):
        product_name = self.return_text_of_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message,  'The name in message differs from real product name'

    def product_price_in_message(self):
        product_price = self.return_text_of_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, 'The price in message differs from real product price'

    # functions that check if it is  the right page
    def should_be_url_attribute(self):
        assert ProductPageLocators.URL_ATTRIBUTE in self.browser.current_url, "An address URL is wrong"
        print(self.browser.current_url)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'There is no "Add to basket" ' \
                                                                                   'button on the page'
