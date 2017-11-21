import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def isElementExist(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
