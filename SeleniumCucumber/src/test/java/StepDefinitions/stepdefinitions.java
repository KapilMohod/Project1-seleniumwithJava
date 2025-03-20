package StepDefinitions;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.*;
import junit.framework.Assert;

public class stepdefinitions {
	
	WebDriver driver;

	@Given("Open the chrome browser")
	public void open_the_chrome_browser() 
	{
	    System.setProperty("webdriver.chrome.driver", "D://Asus//eclipse//SeleniumCucumber//Drivers//chromedriver.exe");
	    driver = new ChromeDriver();
	    
	}

	@When("I open the LinkedIn Page")
	public void i_open_the_linked_in_page() 
	{
	    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin");
	}

	@Then("I verify that Logo is present on Page")
	public void i_verify_that_logo_is_present_on_page() 
	{
	   boolean Logo = driver.findElement(By.xpath("//*[@id='linkedin-logo']")).isDisplayed();
	   Assert.assertEquals(true, Logo);
	   
	}

	@Then("Closed the browser")
	public void closed_the_browser() 
	{
	   driver.quit();
		
	}
}
