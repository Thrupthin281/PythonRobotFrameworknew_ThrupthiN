*** Settings ***

Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***

Verify_google_application

    Open Browser  https://www.google.com/  chrome
    Maximize Browser Window
    Close Browser

