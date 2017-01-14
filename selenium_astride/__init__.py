# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

__version__ = '0.2.1'


class BasePage(object):
    def __init__(self, driver, trace=False):
        self.driver = driver
        self.trace = trace

    def _get_trace(self):
        return self.driver.page_source if self.trace else None

    def _click_action(self, locator, timeout=10.0):
        driver = self.driver
        try:
            element = WebDriverWait(driver, float(timeout)).until(EC.element_to_be_clickable(locator),
                                                                  self._get_trace())
        except StaleElementReferenceException:
            driver.implicitly_wait(2)
            element = WebDriverWait(driver, float(timeout)).until(EC.element_to_be_clickable(locator),
                                                                  self._get_trace())
        element.click()

    def _wait_for_element(self, locator, timeout=10.0):
        driver = self.driver
        WebDriverWait(driver, float(timeout)).until(
            EC.presence_of_element_located(locator), self._get_trace())
        return driver.find_element(*locator)


class BasePageNamedElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element


class BasePageCSSElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_css_selector(self.locator))
        driver.find_element_by_css_selector(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_css_selector(self.locator))
        element = driver.find_element_by_css_selector(self.locator)
        return element
