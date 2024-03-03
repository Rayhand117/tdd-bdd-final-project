"""
Environment for Behave Testing
"""
import os
from os import getenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')

def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Set the path for ChromeDriver
    os.environ["webdriver.chrome.driver"] = "/usr/bin/chromedriver"
    # Instantiate the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox") # Bypass OS security model
    options.add_argument("--headless")
    context.driver = webdriver.Chrome(service=Service(os.environ["webdriver.chrome.driver"]), options=options)
    context.driver.implicitly_wait(context.wait_seconds)

def after_all(context):
    """ Executed after all tests """
    if hasattr(context, 'driver'):
        context.driver.quit()

######################################################################
# Utility functions to create web drivers
######################################################################

def get_chrome():
    """Creates a headless Chrome driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)


def get_firefox():
    """Creates a headless Firefox driver"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)    
    