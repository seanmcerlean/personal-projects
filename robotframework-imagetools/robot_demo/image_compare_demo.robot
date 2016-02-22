*** Settings ***
Library  ../ImageTools/

*** Test Cases ***
Compare Identical Images By Pixels
    ${diff}=  Compare Image Files  robot1.png  robot3.png
    Should Be True  ${diff} == 0

Compare Different Images By Pixels
    ${diff}=  Compare Image Files  robot1.png  robot2.png
    Should Be True  ${diff} > 4

Compare Identical Images By Histogram
    ${diff}=  Compare Image Files  robot1.png  robot3.png  algorithm=histogram
    Should Be True  ${diff} == 0

Compare Different Images By Histogram
    ${diff}=  Compare Image Files  robot1.png  robot2.png  algorithm=histogram
    Should Be True  ${diff} > 950

Non Existing File returns An Error String
    ${diff}=  Compare Image Files  robot1.png  robot4.png
    Should Be Equal  ${diff}  Error reading one or more files

