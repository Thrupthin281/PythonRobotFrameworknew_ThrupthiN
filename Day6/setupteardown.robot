*** Settings ***
Library     SeleniumLibrary
#Suite Setup     Launch_My_Browser
#Suite Teardown  Close_My_Browser

Test Setup  Launch_My_Browser
Test Teardown   Close_My_Browser
*** Variables ***

*** Test Cases ***

Validate_Google_Logo
    Wait Until Page Contains Element    xpath:(//div[@class='example'])[4]//label[1]

#Validate_Google_Logo
    #Wait Until Page Contains Element    xpath:(//input[@name='btnK'])[2]


#   Validate Check box 1 is not checked

    #Checkbox Should Not Be Selected    xpath:(//input[@type='checkbox'])[1]
    #Sleep    2

#   Validate Check box 2 is checked

    #Checkbox Should Be Selected    xpath:(//input[@type='checkbox'])[2]
    #Sleep    2

#   Check the Check box 1
    #Select Checkbox    xpath:(//input[@type='checkbox'])[1]
    #Sleep    2

#   Now Check box 1 is checked
    #Checkbox Should Be Selected    xpath:(//input[@type='checkbox'])[1]
    #Sleep    2

#   UnCheck check box 2
    #Unselect Checkbox    xpath:(//input[@type='checkbox'])[2]
    #Sleep    2

#   Now Check Check box 2 is not checked
    #Checkbox Should Not Be Selected    xpath:(//input[@type='checkbox'])[2]
    #Sleep    2


    Scroll Element Into View    //h3[text()='Initialize by JavaScript']
    Sleep    2
    Wait Until Page Contains Element    xpath:(//div[@class='example'])[4]//label[1]
    Click Element    xpath:(//div[@class='example'])[4]//label[1]
    Sleep    2
    Click Element    xpath:(//div[@class='example'])[4]//label[2]
    Sleep    2
    Click Element    xpath:(//div[@class='example'])[4]//label[1]


*** Keywords ***
Launch_My_Browser

    Open Browser    https://www.bootstraptoggle.com/     Chrome
    Maximize Browser Window
    Sleep    2


Close_My_Browser

    Close All Browsers
