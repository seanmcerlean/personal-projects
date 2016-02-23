*** Settings ***
Library  ../ImageTools/

*** Test Cases ***
Get Image Width
    ${width}=  Get Image Width  robot1.png
    Should Be True  ${width} == 400

Get Image Height
    ${height}=  Get Image Height  robot1.png
    Should Be True  ${height} == 400

Get Image Size
    ${size}=  Get Image Size  robot1.png
    Should Be True  ${size} == (400, 400)

Crop Image
    Crop Image   robot1.png  left=0  upper=0  right=20  lower=20
    ${size}=  Get Image Size  robot1_cropped.png
    Should Be True  ${size} == (20, 20)

Resize Image
    Resize Image  robot1.png  width=250  height=450
    ${size}=  Get Image Size  robot1_resized.png
    Should Be True  ${size} == (250, 450)