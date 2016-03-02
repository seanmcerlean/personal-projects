*** Settings ***
Documentation    Interactions with the Gruyere home page
...              Note as google generates instances for each user, the HOME_URI will need updated

*** Variables ***
${SIGN_IN_URI}      login
${SIGN_IN_TITLE}    Gruyere: Login

${HOME_LINK}        Home
${SIGN_IN_LINK}     Sign in
${SIGN_UP_LINK}     Sign up

&{USER_FIELD}       loc=name  value=uid
&{PASS_FIELD}       loc=name  value=pw
${SUBMIT_BUTTON}    Login

${FAILED_LOGIN_TEXT}  Invalid user name or password.

*** Keywords ***
_Enter ${text} In Username Field
    Input text    &{USER_FIELD}[loc]=&{USER_FIELD}[value]  ${text}

_Enter ${text} In Password Field
    Input text    &{PASS_FIELD}[loc]=&{PASS_FIELD}[value]  ${text}

_Submit Credentials
    Click button  ${SUBMIT_BUTTON}

Enter ${username} and ${password}
    _Enter ${username} In Username Field
    _Enter ${password} In Password Field
    _Submit Credentials
