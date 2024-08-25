import time

from pages.base_page import BasePage
from pages.product_locators import ProductLocators
import time
class Product_Page(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductLocators.BASKET)
        cart.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductLocators.NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductLocators.NAME).text
        message = self.browser.find_element(*ProductLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductLocators.MESSAGE_PRICE), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductLocators.PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductLocators.MESSAGE_PRICE).text
        product_price = self.browser.find_element(*ProductLocators.PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"