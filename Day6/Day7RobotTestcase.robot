*** Settings ***
Library     SeleniumLibrary


*** Variables ***


*** Test Cases ***

CheckboxDropdown_Selection

    Open Browser    https://codepen.io/RobotsPlay/pres/pyNLdL    Chrome
    Maximize Browser Window
    Sleep    2

    Select Frame    id:result
    Wait Until Page Contains Element    xpath://div[@class='dropdown']
    Sleep    2
    Click Element    xpath://div[@class='dropdown']
    Sleep    2
    Click Element    xpath://input[@value='Selection 1']
    Sleep    2
    Click Element    xpath://input[@value='Selection 2']
    Sleep    2
    Click Element    xpath://input[@value='Selection 3']
    Sleep    2
    Unselect Frame
    Sleep    2





    Close All Browsers



*** Keywords ***