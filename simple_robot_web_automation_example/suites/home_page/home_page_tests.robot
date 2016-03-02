*** Settings ***
Documentation    Test For The Gruyere Homepage

Resource         ../../keywords/common/browser/browser.robot
Resource         ../../keywords/page_resources/home/home_page.robot

Suite Setup      Open Browser For Testing
Suite Teardown   Close All Browsers

*** Test Cases ***
Homepage Title Displays Correctly
    Go To  ${HOST}
    Title Should Be  ${HOME_TITLE}

Homepage Contains Expected Contact
    Go To  ${HOST}
    Content Table Contains Cheddar Mac
    Content Table Contains Brie

Home Link Returns To Same Page
    Go To  ${HOST}
    Click Home
    Title Should Be  ${HOME_TITLE}