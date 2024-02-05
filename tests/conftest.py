import logging
import os.path
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.ConfigurationReader import read_config
from selenium.webdriver.chrome.options import Options
from utilities.LogUtils import Logger

logger = Logger()
log = logger.logger_setup(logging.DEBUG)
url = None
driver = None


@pytest.fixture(scope="class")
def setup_and_teardown(request, browser, environment):
    log.info("Setting up the webdriver.")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = browser.lower()
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome-headless":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError("Please provide browser from chrome/edge/firefox/chrome-headless.")

    driver.maximize_window()
    global url
    env = environment.lower()
    if env == "qa":
        url = read_config("BASIC INFO", "URL")
    elif env == "stage":
        url = read_config("BASIC INFO", "PRACTICE_URL")
    elif env == "prod":
        url = read_config("BASIC INFO", "GLASSWALL_URL")
    else:
        raise ValueError("Please provide valid env from qa/stage/prod.")

    driver.get(url)
    request.cls.driver = driver
    yield
    log.info("Tearing down webdriver")
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_step", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
    

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Python Selenium-Pytest Report"
