*** Settings ***
Library     SeleniumLibrary
Library     ../Reusable/pom.py
Library     String

*** Variables ***
${expectedstringInURL}      software-testing-agency-contact

*** Test Cases ***

#TestCase1_Validation

    #read_XML_Test_Data
    #Open Browser    ${url}      ${browser}
    #Maximize Browser Window
    #TestCase1_Validation

#TestCase2_Validation

    #read1_XML1_Test1_Data1
    #Open Browser    ${url}      ${browser}
    #Maximize Browser Window


TestCase3_Validation

    read2_XML2_Test2_Data2
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
    Sleep    2
    Scroll Element Into View    xpath://h2[text()='CLIENT SAYS']
    Sleep    2

    Wait Until Page Contains Element    xpath://h2[text()='CLIENT SAYS']
    Sleep    2
    ${currentclienturl}=     Get Text    xpath://li[@class='testimonial_content flex-active-slide']//p/span[2]
    Set Global Variable    ${currentclienturl}
    Log To Console    ${currentclienturl}
    Scroll Element Into View    xpath://a[@class='flex-next']
    Sleep    2
    Click Element    xpath://a[@class='flex-next']
    Sleep    3
    ${nextclienturl}=     Get Text    xpath://li[@class='testimonial_content flex-active-slide']//p/span[2]
    Log To Console    ${nextclienturl}
    Should Not Be Equal    """${currentclienturl}"""    """${nextclienturl}"""





    Sleep   2
    ${Currentclienturl}=    Get Text    xpath://li[@class='testimonial_content flex-active-slide']//p/span[2]

    Set Global Variable     ${Currentclienturl}

    Log To Console  ${Currentclienturl}


    Scroll Element Into View    xpath://a[@Class='flex-prev']

    Sleep    3
    

    Click Element    xpath://a[@Class='flex-next']

    Sleep    3

    ${Nextclienturl}=   Get Text    xpath://li[@class='testimonial_content flex-active-slide']//p/span[2]

    Log To Console  ${Nextclienturl}

    Should Not Be Equal     """${Currentclienturl}"""   """${Nextclienturl}"""

    #Click Element    xpath://a[@class='flex-prev']
    #Sleep    3
    #${prevclienturl}=     Get Text    xpath://li[@class='testimonial_content flex-active-slide']//p/span[2]
    #Log To Console    ${prevclienturl}
    #Should Be Equal    """${currentclienturl}"""    """${prevclienturl}"""
    #Sleep    2



    Close All Browsers





*** Keywords ***
read2_XML2_Test2_Data2

    ${url}     pom.readXML    url
    ${browser}     pom.readXML    browser
    Set Global Variable    ${url}
    Set Global Variable    ${browser}





*** Keywords ***
read_XML_Test_Data

    ${url}     pom.readXML    url
    ${browser}     pom.readXML    browser
    ${FleekTopMenuBars}    pom.readXML    FleekTopMenuBars
    ${ServicessubMenuOption}    pom.readXML    ServicessubMenuOption
    Set Global Variable    ${url}
    Set Global Variable    ${browser}
    Set Global Variable    ${FleekTopMenuBars}
    Set Global Variable    ${ServicessubMenuOption}

TestCase1_Validation

    Sleep    2
    Wait Until Page Contains Element    xpath://img[@class='mobile']
    Sleep    2
    @{FleekTopMenuBars}=    Split String    ${FleekTopMenuBars}     ,

    FOR    ${ele}    IN    @{FleekTopMenuBars}
        Log    ${ele}
        Log To Console    ${ele}
        ${runtimeXpath}=     pom.FleekTopMenuBars    ${ele}
        Log To Console    ${runtimeXpath}
        Wait Until Page Contains Element   ${runtimeXpath}

    END

    # Mousehover on 'Services' and Validate the sublinks

    Mouse Over    xpath://nav[@class='main_menu drop_down right']/ul/li/a/span[text()='Services']
    Sleep    2
    @{ServicessubMenuOption}=    Split String    ${ServicessubMenuOption}       ,

    FOR    ${ele}    IN    @{ServicessubMenuOption}
        Log    ${ele}
        Log To Console    ${ele}
        ${runtimeXpath}=     pom.ServicessubMenuOption    ${ele}
        Log To Console    ${runtimeXpath}
        Wait Until Page Contains Element   ${runtimeXpath}

    END


*** Keywords ***

read1_XML1_Test1_Data1

    ${url}     pom.readXML    url
    Set Global Variable    ${url}
    ${browser}     pom.readXML    browser
    Set Global Variable    ${browser}
    ${FirstName}=   pom.readXML    FirstName
    Set Global Variable    ${FirstName}
    ${LastName}=   pom.readXML    LastName
    Set Global Variable    ${LastName}
    ${email}=   pom.readXML    email
    Set Global Variable    ${email}
    ${phone}=   pom.readXML    phone
    Set Global Variable    ${phone}
    ${Subject}=   pom.readXML    Subject
    Set Global Variable    ${Subject}
    ${Message}=   pom.readXML    Message
    Set Global Variable    ${Message}


Fill_ContactUs_Form
    Input Text    //input[@name='your-name']    ${FirstName}

    Input Text    //input[@name='LastName']    ${LastName}

    Input Text    //input[@name='your-email']    ${email}

    Input Text    //input[@name='your-phone']    ${phone}

    Input Text    //input[@name='your-subject']    ${Subject}

    Input Text    //textarea[@name='your-message']    ${Message}

TestCase2_Validation


    read1_XML1_Test1_Data1
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
    TestCase2_Validation
    Sleep    5
    Wait Until Page Contains Element    xpath:(//span[contains(text(),'Contact Us')])[1]
    Click Element    xpath:(//span[contains(text(),'Contact Us')])[1]
    Sleep    2
    ${runtimeurl}   Get Location
    Should Be True    "software-testing-agency-contact" in"""${runtimeurl}"""
    Fill_ContactUs_Form
    Sleep    5
    ${netherlandaddress}    Get Text    xpath://h2[text()='THE NETHERLANDS']/following-sibling::p[1]
    Should Be True    "Vijzelstraat 68-78" in """${netherlandaddress}"""
    Should Be True    "1017 HL | Amsterdam" in """${netherlandaddress}"""
    Should Be True    "The Netherlands" in """${netherlandaddress}"""


    Close All Browsers