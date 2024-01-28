import logging
import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utilities.ConfigurationReader import read_homePageLocators
from utilities.LogUtils import Logger


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    logger = Logger()
    log = logger.logger_setup()

    searchBox = read_homePageLocators("SEARCHBOX_INPUT")
    closeBtn = read_homePageLocators("CLOSE_BTN")
    fromInput = read_homePageLocators("FROM_INPUT")
    toInput = read_homePageLocators("TO_INPUT")

    def search(self, text):
        self.log.info("Entering the text.")
        self.input_text(self.searchBox, text)
        self.press_enterKey(self.searchBox)
        self.log.info("Searching for the result")
        self.log.info(f"Title is: {self.get_title()}")
