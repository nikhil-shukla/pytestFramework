import logging
import pytest
import allure
import time
from allure_commons.types import AttachmentType
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities.CSVReader import ReadCSV
from utilities.LogUtils import Logger

@allure.title("Test Webapp")
@allure.description("This test attempts to search something and check for the title.")
@allure.tag("Web", "Search")
@allure.label("owner", "Nikhil")
@allure.link("https://www.google.com/", name="Website")
@allure.testcase("TC-121")
class TestSearch(BaseTest, ReadCSV):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage = HomePage(self.driver)
        self.logger = Logger()
        self.log = self.logger.logger_setup(logging.DEBUG)

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    def test_checkTitle(self):
        time.sleep(3)
        title = self.driver.title
        assert title == "Google"

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_checkTitleNegative(self):
        time.sleep(3)
        title = self.driver.title
        assert title == "Google1"

    @pytest.mark.skip
    @allure.severity(allure.severity_level.MINOR)
    def test_search(self):
        search_text = ReadCSV.read_csv_by_id('1', 'search_text')
        time.sleep(5)
        self.homepage.search(search_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="test_search", attachment_type=AttachmentType.PNG)

    @pytest.mark.skip
    @pytest.mark.parametrize("search_string", ["Pytest", "Selenium"])
    @allure.severity(allure.severity_level.NORMAL)
    def _parameterizeSearch(self, search_string):
        time.sleep(5)
        self.homepage.search(search_string)
        title = self.driver.title
        self.log.info(f"Title is {title}")
        assert search_string in title
