Feature: Login  

  Scenario Outline: Verify Login with Multiple Credentials  

    Given User opens the Chrome browser  
    When User navigates to the LinkedIn login page  
    And User enters "<username>" and "<password>"  
    And Clicks on the Sign In button    

    Examples:  
      | username                 | password  |  
      | kapilmohod25@gmail.com   | kapil@25 |  
      
   
    	