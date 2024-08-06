from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert driver.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.login), "Login mistake"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert  self.browser.find_element(*LoginPageLocators.password), "Password mistake"