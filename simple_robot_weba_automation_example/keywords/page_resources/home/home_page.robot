*** Settings ***
Documentation    Interactions with the Gruyere home page
...              Note as google generates instances for each user, the HOME_URI will need updated

*** Variables ***
${HOME_TITLE}     Gruyere: Home

${HOME_LINK}      Home
${SIGN_IN_LINK}   Sign in
${SIGN_UP_LINK}   Sign up
${REFRESH_LINK}   Refresh

&{CONTENT_TABLE}  loc=css  value=body > div.content

*** Keywords ***
Click Home
   Click Link  ${HOME_LINK}

Go To Sign In Page
   Click Link  ${SIGN_IN_LINK}

Go To Sign Up Page
   Click Link  ${SIGN_UP_LINK}

Refresh Content
   Click Link  ${REFRESH_LINK}

Content Table Contains ${value}
    Element Should Contain  &{CONTENT_TABLE}[loc]=&{CONTENT_TABLE}[value]  ${value}