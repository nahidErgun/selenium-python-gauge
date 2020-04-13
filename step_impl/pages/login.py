from selenium.webdriver.common.by import By
from step_impl.base_test import driver
from getgauge.python import step, before_scenario, Messages
from step_impl.pages.base_page_util import click,set,isExist,clickElementsByIndex

LOGINURL = (By.ID, 'headerLoginUrl')
EMAILTAB = (By.CLASS_NAME, 'gaClickEvent')
EMAILFIELD = (By.ID, 'email')
PASSWORDFIELD = (By.ID, 'password')
LOGINBUTTON = (By.CLASS_NAME, 'confirm')
ACCOUNT = (By.ID, 'account')

@step("Click login button")
def clickLoginButton():
    click(LOGINURL)

@step("Select email as login type")
def selectEmailForLogin():
    clickElementsByIndex(EMAILTAB,1)
    
@step("Set email <username>")
def setEmail(username):
        set(EMAILFIELD, username)

@step("Set password <password>")
def setPassword(password):    
    set(PASSWORDFIELD, password)

@step("Click login button then check that user is logged in")
def clickLoginAndCheckSuccess():
    click(LOGINBUTTON)
    assert  True == isExist(ACCOUNT),"Login fail"