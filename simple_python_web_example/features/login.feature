Feature: Invalid Login Handling

  Scenario Outline:
    Given I am on the login page
    When I enter <username> and <password>
    And I press the login button
    Then I see the message <error_message>

    Examples:
    |username|password|error_message|
    |foo     |foo     |Incorrect image validation text.          |
    |' or 1=1|' or 1=1| Incorrect image validation text.         |

