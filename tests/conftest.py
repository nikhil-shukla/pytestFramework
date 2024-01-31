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
def setup_and_teardown(request, browser):
    log.info("Setting up the webdriver.")
    browser = read_config("BASIC INFO", "BROWSER")
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
    else:
        raise ValueError("Please provide browser from chrome/edge/firefox.")

    driver.maximize_window()
    global url
    url = read_config("BASIC INFO", "URL")
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


def environment(request):
    return request.config.getoption("--env")


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])

#     if report.when == 'call' or report.when == "setup":
#         extra.append(pytest_html.extras.url(url))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             _capture_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Python Selenium-Pytest Report"
