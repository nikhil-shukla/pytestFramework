import logging
import pytest
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities.CSVReader import ReadCSV
from utilities.LogUtils import Logger


class TestSearch(BaseTest, ReadCSV):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.homepage = HomePage(self.driver)
        self.logger = Logger()
        self.log = self.logger.logger_setup(logging.DEBUG)

    # @pytest.mark.skip
    def test_checkTitle(self):
        title = self.driver.title
        assert title == "Google"

    # @pytest.mark.skip
    def test_search(self):
        search_text = ReadCSV.read_csv_by_id('1', 'search_text')
        self.homepage.search(search_text)

    @pytest.mark.parametrize("search_string", ["Pytest", "Selenium"])
    def test_parameterizeSearch(self, search_string):
        self.homepage.search(search_string)
        title = self.driver.title
        self.log.info(f"Title is {title}")
        assert search_string in title
