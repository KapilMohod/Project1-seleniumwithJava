Feature: Search Bar

  Scenario Outline: To Test the Search Functionality
    Given User opened the Chrome browser  
    When User navigates to the LinkedIn Sign In page  
    When User enters linkedin_credentials "<username>" and "<password>"  
    When User clicks on the Login button    
    Then User navigates to the homepage
    When User searches "<search>" as per requirement & search it
    And User clicks on the People button
    Then People related to search should be displayed

  Examples:  
    | username                 | password  | search         |
    | kapilmohod25@gmail.com   | kapil@25  | Test Engineer  |
