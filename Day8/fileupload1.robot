*** Settings ***
Library     SeleniumLibrary
Library     ../Reusable/pom.py
#Suite Setup     Launch_My_Browser
#Suite Teardown  Close_My_Browser

Test Setup  Launch_My_Browser
Test Teardown   Close_My_Browser
*** Variables ***

# This is for Laptop branch

*** Test Cases ***

Validate_FILE_UPLOAD

# C:\Users\00004999\PycharmProjects\robot scripts\pythonProject\Day1PythonProgramming\Reports\selenium-screenshot-1.png
    ${myImagePath}  pom.myImagePath    selenium-screenshot-1.png
    Choose File    file-upload    ${myImagePath}
    Sleep    4

    Click Element    file-submit
    Sleep    10

*** Keywords ***
Launch_My_Browser

    Open Browser    https://the-internet.herokuapp.com/upload     Chrome
    Maximize Browser Window
    Sleep    2


Close_My_Browser

    Close All Browsers
