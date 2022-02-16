from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(BasePage):
    URL_ATTRIBUTE = 'promo='
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    # PRODUCT_PRICE = (By.CSS_SELECTOR, ".table-striped tr:nth-of-type(4) td")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-of-type(3) strong")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-of-type(1) strong")
