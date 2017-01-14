from selenium.webdriver.common.by import By


class HomeLocators(object):
    FIRST_ENTRY_TITLE = (By.CSS_SELECTOR, ".entries > li > h2 ")
    LOGIN = (By.CSS_SELECTOR, '.metanav > a')

class LoginLocators(object):
    TITLE = (By.CSS_SELECTOR, "h2")
    SUBMIT = (By.CSS_SELECTOR, "#login")
    ERROR = (By.CSS_SELECTOR, ".error")
