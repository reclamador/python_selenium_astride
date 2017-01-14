from selenium_astride import BasePage, BasePageCSSElement, BasePageNamedElement
from .locators import HomeLocators, LoginLocators

class HomePage(BasePage):

    def go_login(self):
        self._click_action(HomeLocators.LOGIN)

    def first_entry(self):
        element = self._wait_for_element(HomeLocators.FIRST_ENTRY_TITLE, 1)
        return element.text


class UsernameElement(BasePageCSSElement):
    locator = "#username"

class PasswordElement(BasePageNamedElement):
    locator = "password"

class LoginPage(BasePage):
    username = UsernameElement()
    password = PasswordElement()

    def title_page(self):
        element = self._wait_for_element(LoginLocators.TITLE, 1)
        return element.text

    def login(self):
        self._click_action(LoginLocators.SUBMIT)

    def get_error(self):
        element = self._wait_for_element(LoginLocators.ERROR, 1)
        return element.text
