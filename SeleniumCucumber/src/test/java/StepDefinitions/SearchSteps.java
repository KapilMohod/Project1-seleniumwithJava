package StepDefinitions;

import java.time.Duration;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import PageObject.SearchBar;
import io.cucumber.java.en.*;

public class SearchSteps 
{
	public WebDriver driver;
	public SearchBar sp;
	
	@Given("User opened the Chrome browser")
	public void user_opened_the_chrome_browser() 
	{
	   System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir")+"//Drivers//chromedriver.exe");
	   driver = new ChromeDriver();
	   sp = new SearchBar(driver);  
	   
	}

	@When("User navigates to the LinkedIn Sign In page")
	public void user_navigates_to_the_linked_in_Sign_In_page() 
	{
	    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin");
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
	    driver.manage().window().maximize();
	}
	
	@When("User enters linkedin_credentials {string} and {string}")
	public void user_enters_linkedin_credentials_and(String Email, String Password) throws InterruptedException 
	{
		sp.Addusername(Email);
	    sp.Addpassword(Password);
	    
	    Thread.sleep(5000);
	}

	@When("User clicks on the Login button")
	public void user_clicks_on_the_login_button() 
	{
		sp.Sign_InButton();
	}
	
	@Then("User navigates to the homepage")
	public void user_navigates_to_the_homepage() 
	{
		System.out.println("The Logo is displayed");
	   
	}
	
	@When("User searches {string} as per requirement & search it")
	public void user_searches_as_per_requirement(String Content) throws InterruptedException 
	{
		sp.Searching(Content);
		Thread.sleep(5000);
	    
	}
	
	@And("User clicks on the People button")
	public void user_clicks_on_the_people_button() throws InterruptedException 
	{
	    sp.People();
	    Thread.sleep(3000);
	}
	
	@Then("People related to search should be displayed")
	public void people_related_to_search_should_be_displayed() 
	{
	   sp.displayPeopleResults();
	}

}
