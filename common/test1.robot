*** Settings ***
Documentation    Suite description
Library           Selenium2Library
Library    ../common_lib/WinRemote.py

*** Test Cases ***
Test title
    ${result} =  Run Commond
    Log    ${result}
    log to console  ${result}
    Open Browser    https://www.baidu.com    chrome
    Sleep    1
    Input Text    xpath=//*[@id="kw"]    123
    Click Button     xpath=//*[@id="su"]
    Sleep     2
    Close browser


