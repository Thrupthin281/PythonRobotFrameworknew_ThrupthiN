from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

"""
class Day2TestScripts:


    def launchmychromebrowser(self):
        driver = webdriver.Chrome("C:/Users/00004999/Desktop/browsers/chromedriver")
        driver.get("https://www.google.com")
        driver.maximize_window()

        I_AmFeeling_lcy = driver.find_element(By.NAME, "btnl")
        I_AmFeeling_lcy.is_displayed()
        print("Google Page I_AmFeeling_lcy is getting displayed..")

        # button = driver.find_element(By.XPATH , "// MyTestPath")
        google_logo = driver.find_element(By.CLASS_NAME, "lnXdpd")
        google_logo.is_displayed()
        print("Google Page logo is displayed")

        search_in_google = driver.find_element(By.NAME, "q")
        search_in_google.send_keys("Robot Framework")
        sleep(5)
        print("Google Page logo is displayed")

        # button.click()

        driver.quit()
        print("Google")


obj = Day2TestScripts()
obj.launchmychromebrowser()

"""


class Day2TestScripts:

    def techedtrainings(self):
        driver = webdriver.Chrome("C:/Users/00004999/Desktop/browsers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://techedtrainings.com/contact/")
        driver.maximize_window()
        submitbuttonpro = driver.find_element(By.XPATH, "//button[contains(.,'submit')]")
        print("The font Family of Submit button is :" + submitbuttonpro.value_of_css_property("font-family"))


obj = Day2TestScripts()
obj.techedtrainings()