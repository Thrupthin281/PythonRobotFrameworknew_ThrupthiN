*** Settings ***
Library     SeleniumLibrary
Library    Dialogs
*** Variables ***
${expectedurl}  https://www.webucator.com/
${expecteTitle}     "Online and Onsite Instructor-led Training Classes | Webucator"


*** Test Cases ***

Webucator_Application_Testing

        Open Browser        https://www.webucator.com/       Chrome
        Maximize Browser Window
        #check logo
        Wait Until Page Contains Element    xpath://img[@alt='Webucator Logo']
        #check sign in
        Wait Until Page Contains Element    xpath://a[contains(.,' SIGN IN')]
        ${pageurl}=     Get Location
        Log To Console    ${pageurl}
        #verify pageurl
        Should Be True    """${pageurl}"""=="""${expectedurl}"""
        #verify title
        Wait For Condition    return document.title==${expecteTitle}
        Close All Browsers
