*** Settings ***
Library     DateTime


*** Variables ***

*** Test Cases ***
CurrentDate_Test

    ${DateandTime}=     Get Current Date
    Log To Console    ${DateandTime}
    ${DateandTime}=     Add Time To Date    ${DateandTime}      10 days
    Log To Console    ${DateandTime}
    ${DateandTime}=     Add Time To Date    ${DateandTime}      -10 days
    Log To Console    ${DateandTime}

*** Keywords ***