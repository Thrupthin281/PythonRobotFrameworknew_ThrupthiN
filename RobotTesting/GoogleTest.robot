*** Settings ***
Library     SeleniumLibrary

*** Variables ***

*** Test Cases ***

Test_Google_Application
        Open Browser        http://www.google.com       Chrome
        Maximize Browser Window
        #Validate google logo
        Basic_Testing
Test_Google_Application_login
        Open Browser        http://www.google.com       Chrome
        Maximize Browser Window
        #Validate google logo
        Login_Validation

*** Keywords ***

Basic_Testing
    Wait Until Page Contains Element    xpath://img[@alt='Google']
        #Validate google search
        Wait Until Page Contains Element    xpath:(//input[@name='btnK'])[2]
        #Validate i m feeling lucky
        Wait Until Page Contains Element    xpath:(//input[@name='btnI'])[2]
        #Validate google search
        Wait Until Page Contains Element    xpath://input[@name='q']
        Input Text  xpath://input[@name='q']    RobotFramework
        Sleep   10
        Close All Browsers


Login_Validation

        Wait Until Page Contains Element   xpath://a[text()='Sign in']
        Click Element    xpath://a[text()='Sign in']
        Sleep   10
        Wait Until Page Contains    Sign in
        Wait Until Page Contains    Use your Google Account
        Close All Browsers