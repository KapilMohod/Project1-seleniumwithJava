package PageObject;

import static org.junit.Assert.assertEquals;

import java.util.List;

import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SearchBar 
{
	public WebDriver driver;
	
	public SearchBar(WebDriver rdriver)
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
	
	@FindBy (xpath = "//li-icon[@role='img']")
	@CacheLookup
	WebElement Logo;
	
	@FindBy(xpath = "//input[@aria-label='Search']")
	@CacheLookup
	WebElement SearchBar;
	
	@FindBy(xpath = "(//div[@id='search-reusables__filters-bar']/ul/li/button)[3]")
	@CacheLookup
	WebElement Peoples;
	
	@FindBy(xpath = "//div[@id='Ufq6JAWPRY2b55MrR3yWQw==']/div/ul/li")
	@CacheLookup
	List<WebElement> PeopleDisplayed;
	
	
	public void Addusername(String username)
	{
		Username.sendKeys(username);
	}
	
	public void Addpassword(String password)
	{
		Password.sendKeys(password);
	}
	
	public void Sign_InButton()	
	{
		SignIn.click();
	}
	
	public void logo()
	{
		Logo.isDisplayed();
		
	}
	
	public void Searching(String content)
	{
		SearchBar.sendKeys(content + Keys.ENTER);
	}
	
	public void People()
	{
		Peoples.click();
	}
	
	public void displayPeopleResults() 
	{
        System.out.println("People found: " + PeopleDisplayed.size());
        
        for (WebElement person : PeopleDisplayed) 
        {
            System.out.println(person.getText());
        }
	}


}
