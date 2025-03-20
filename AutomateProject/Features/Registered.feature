Feature: Registration

  Background: commonSteps
    Given User Opens the chrome browser

  Scenario Outline: : Valid Registration
    When User navigates the Registration page
    Then User Verified the Title
    Then User Enters registration details: "<Name>", "<Email>", "<Phone>", "<Address>"

    Examples:
      | Name | Email        | Phone         | Address       |
      | ABC  | abc@mail.com | +919637358614 | G.Nagar, Amt. |

  Scenario: verify Gender Radio Buttons
      When User navigates the Registration page
      Then User select the gender

