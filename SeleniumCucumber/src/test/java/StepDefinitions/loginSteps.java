package StepDefinitions;

import java.time.Duration;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import PageObject.LoginPage;
import io.cucumber.java.en.*;

public class loginSteps 
{
	
	public WebDriver driver;
	public LoginPage lp;
	
	@Given("User opens the Chrome browser")
	public void user_opens_the_chrome_browser() 
	{
	   System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir")+"//Drivers//chromedriver.exe");
	   driver = new ChromeDriver();
	   lp = new LoginPage(driver);  
	   
	}

	@When("User navigates to the LinkedIn login page")
	public void user_navigates_to_the_linked_in_login_page() 
	{
	    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin");
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
	    driver.manage().window().maximize();
	}

	@When("User enters {string} and {string}")
	public void user_enters_and(String Email, String Password) throws InterruptedException 
	{
	    lp.Enterusername(Email);
	    lp.Enterpassword(Password);
	    
	    Thread.sleep(5000);
	}

	@When("Clicks on the Sign In button")
	public void clicks_on_the_sign_in_button() 
	{
	    lp.SignInButton();
	}


}
