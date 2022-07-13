*** Settings ***
Library    SeleniumLibrary
Library    String
Library     ../Reusable/pom.py

*** Variables ***
${pop_cow}  Data Science Course,Artificial Intelligence Course,Machine Learning Certification Course,Python Certification
${url}   https://intellipaat.com/
${browsername}  headlesschrome
# //h4[text()='Popular Courses']/following-sibling::p[1]/a[text()='Data Science Course']


*** Test Cases ***

Validate_Dynamic_Web_Element

    Open Browser    ${url}  ${browsername}
    Sleep    2
    Maximize Browser Window
    Sleep    2

    # Split Popular Courses

    @{subpopularlinks}=  Split String    ${pop_cow}  ,

    # To iterate through the String of Array
    FOR    ${ele}    IN    @{subpopularlinks}
        Log    ${ele}
        #Log To Console    ${ele}
        ${runtimeXpath}=     pom.PopularCoursesSubLinksXpath    ${ele}
        Log To Console    ${runtimeXpath}
        Wait Until Page Contains Element   ${runtimeXpath}
         
    END

    Close All Browsers


*** Keywords ***