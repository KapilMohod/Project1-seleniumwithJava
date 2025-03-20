package PageObject;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
	
	public WebDriver driver;
	
	public LoginPage(WebDriver rdriver)
	{
		driver = rdriver;
		PageFactory.initElements(rdriver, this);
	}
	
	@FindBy (id = "username")
	@CacheLookup
	WebElement Username;
	
	@FindBy (id = "password")
	@CacheLookup
	WebElement Password;
	
	@FindBy (xpath = "//button[@aria-label='Sign in']")
	@CacheLookup
	WebElement SignIn;
	
	
	public void Enterusername(String username)
	{
		Username.sendKeys(username);
	}
	
	public void Enterpassword(String password)
	{
		Password.sendKeys(password);
	}
	
	public void SignInButton()	
	{
		SignIn.click();
	}
	
}
