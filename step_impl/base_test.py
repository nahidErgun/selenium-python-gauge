from selenium import webdriver
from getgauge.python import step, before_scenario, after_scenario, Messages
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome('step_impl/driver/chromedriver')
@before_scenario
def beforescenario():

    driver.maximize_window()
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options = webdriver.ChromeOptions()
    driver.implicitly_wait(15)
    driver.get('https://www.modanisa.com')

@after_scenario
def afterScenario():
    driver.quit()