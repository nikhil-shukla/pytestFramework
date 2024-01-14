import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.LogUtils import Logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    logger = Logger()
    log = logger.logger_setup(logging.DEBUG)

    def get_element(self, locator):
        element = None
        strategy, value = locator.split("_")
        strategy = strategy.lower()
        if strategy == "id":
            element = self.driver.find_element(By.ID, value)
        elif strategy == "name":
            element = self.driver.find_element(By.NAME, value)
        elif strategy == "classname":
            element = self.driver.find_element(By.CLASS_NAME, value)
        elif strategy == "linktext":
            element = self.driver.find_element(By.LINK_TEXT, value)
        elif strategy == "xpath":
            element = self.driver.find_element(By.XPATH, value)
        elif strategy == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, value)
        elif strategy == "partiallinktext":
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif strategy == "tagname":
            element = self.driver.find_element(By.TAG_NAME, value)
        else:
            raise ValueError(f"Invalid locator strategy: {strategy.upper()}")
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()
        self.log.info("Clicked the webelement.")

    def input_text(self, locator, text):
        element = self.get_element(locator)
        element.click()
        time.sleep(2)
        element.clear()
        time.sleep(2)
        element.send_keys(text)
        self.log.info(f"Entered the text.")

    def press_enterKey(self, locator):
        element = self.get_element(locator)
        element.send_keys(Keys.ENTER)
        self.log.info(f"Pressed the Enter key.")

    def get_title(self):
        return self.driver.title

    def check_element_displayed(self, locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def wait_for_element_clickable(self, timeout=5, locator=None):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((self.get_element(locator)))
            )
            self.log.info(f"Element = {locator} can be clicked")
            return element
        except Exception:
            self.log.info(f"Element = {locator} CANNOT be clicked")
            raise
