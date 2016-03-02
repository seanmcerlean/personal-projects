*** Settings ***
Documentation    Test For The Gruyere Homepage

Resource         ../../keywords/common/browser/browser.robot
Resource         ../../keywords/page_resources/sign_in/sign_in_page.robot

Suite Setup      Open Browser For Testing
Suite Teardown   Close All Browsers

Test Template    Sign In And Check For Invalid Login Response

*** Test Cases ***
Failed Login       notauser  notapassword
Missing Username   ${EMPTY}  notapassword
Missing Password   notauser  ${EMPTY}
Both Empty         ${EMPTY}  ${EMPTY}
SQL Injection      ' OR 1=1  ' OR 1=1

*** Keywords ***
Sign In And Check For Invalid Login Response
    [Arguments]  ${username}  ${password}
    Go To  ${HOST}/${SIGN_IN_URI}
    Enter ${username} and ${password}
    Page Should Contain  ${FAILED_LOGIN_TEXT}