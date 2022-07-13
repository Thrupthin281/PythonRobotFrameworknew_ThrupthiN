from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Reusable import Reusable
from PageObjectModel import SignUpPage


class ReadHTML:

    def testautomationpractice(self):
        driver = webdriver.Chrome("C:/Users/00004999/Desktop/browsers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()

        #   read HTML Table ...

        #   Get total row count?

        print("Total Table Row Count is ==> " + str
        (len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))))

        #   Get Total Column Count?

        print("Total Table Column Count is ==> " + str(
            len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))))

        #   Get Author , Subject , Price as per the BookName

        print("If my BookName is" + " " + Reusable.readXmlTestData("bookName") + " Then  Auther Name is  ==> " +
              driver.find_element(By.XPATH, SignUpPage.autherName(Reusable.readXmlTestData("bookName"))).text)

        print("If my BookName is" + " " + Reusable.readXmlTestData("bookName") + " Then  Subject Name is  ==> " +
              driver.find_element(By.XPATH, SignUpPage.SubjectName(Reusable.readXmlTestData("bookName"))).text)

        print("If my BookName is" + " " + Reusable.readXmlTestData("bookName") + " Then  Price Name is  ==> " +
              driver.find_element(By.XPATH, SignUpPage.Pricing(Reusable.readXmlTestData("bookName"))).text)

        driver.quit()


hml = ReadHTML()
hml.testautomationpractice()
