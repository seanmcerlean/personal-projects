*** Settings ***
Documentation    Keywords to start and close browsers

Library          OperatingSystem
Library          Selenium2Library

Variables        ../../../settings.py

*** Keywords ***
Open Browser For Testing
    Set Environment Variable    DISPLAY    ${XVFB_DISPLAY}
    Open Browser          ${HOST}  &{SELENIUM_OPTIONS}[BROWSER]
    Set Selenium Speed    &{SELENIUM_OPTIONS}[DELAY]
    Set Window Size       &{SELENIUM_OPTIONS}[WIDTH]  &{SELENIUM_OPTIONS}[HEIGHT]