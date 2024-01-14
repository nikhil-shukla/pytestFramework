import os
from configparser import ConfigParser

filepath = os.getcwd()


def read_config(section, key):
    config = ConfigParser()
    config.read(filepath + "//configurations//config.ini")
    return config.get(section, key)


def read_homePageLocators(key):
    section = "HOME PAGE"
    config = ConfigParser()
    config.read(filepath + "//locators//homePage_locators.ini")
    return config.get(section, key)
