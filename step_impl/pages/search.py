from selenium.webdriver.common.by import By
from step_impl.base_test import driver
from getgauge.python import step, before_scenario, Messages
from step_impl.pages.base_page_util import click,set,isExist,clickElementsByIndex

SEARCHFIELD = (By.ID, 'search')
SEARCHBUTTON = (By.ID, 'newHeaderFooter-search')
PRUDUCTIMG = (By.CLASS_NAME, 'product-img')
PRICETEXT = (By.CSS_SELECTOR,'.campaign-badge bdi')
@step("Set <searchKeyword> to search field")
def setTextToSearchField(searchKeyword):
    set(SEARCHFIELD,searchKeyword)
@step("Click search button")
def clickSearchButton():
   click(SEARCHBUTTON)
@step("Check products")
def clickLoginAndCheckSuccess():
    assert True == isExist(PRUDUCTIMG),"No product listed"