import os
from selenium.common.exceptions import NoSuchElementException
from step_impl.base_test import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


def click(element):
    driver.find_element(*element).click()
    return element

def clickElementsByIndex (element,index):
     driver.find_elements(*element)[index].click()
     return element

def set(element, value):
    driver.find_element(*element).click()
    driver.find_element(*element).clear()
    driver.find_element(*element).send_keys(value)
    return element
    
def isExist(element):
    try:
        driver.find_element(*element)
        return True
    except NoSuchElementException:
        return False
