from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Reusablenew import Reusablenew

class TestWebucator:

    def launchwebucatorapplication(self):
        global driver
        driver = webdriver.Chrome(Reusablenew.readXmlTestData("chromepath"))
        #print(Reusablenew.readXmlTestData("chromepath"))
        driver.implicitly_wait(10)
        driver.get(Reusablenew.readXmlTestData("URL"))
        print(Reusablenew.readXmlTestData("URL"))
        #driver.get("https://techedtrainings.com/contact/")
        driver.maximize_window()

    def CloseApplication(self):
        driver.quit()

obj = TestWebucator()
obj.launchwebucatorapplication()
obj.CloseApplication()
