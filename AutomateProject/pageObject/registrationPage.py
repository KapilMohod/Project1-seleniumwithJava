from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class registrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.NAME_FIELD = (By.ID, "name")
        self.EMAIL_FIELD = (By.ID, "email")
        self.PHONE_FIELD = (By.ID, "phone")
        self.ADDRESS_FIELD = (By.ID, "textarea")
        self.wait = WebDriverWait(self.driver, 10)

    def navigateToPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def titleVerification(self):

        actualTitle = self.driver.title
        expectedTitle = "Automation Testing Practice"

        assert actualTitle==expectedTitle, "Title doesn't Matched !!"
        print("Navigated Successfully ..... Title Verified & Matched !!")

    def fillRegistrationForm(self, name, email, Ph_number, address):

        self.wait.until(EC.presence_of_element_located(self.NAME_FIELD)).clear()
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

        self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD)).clear()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

        self.wait.until(EC.presence_of_element_located(self.PHONE_FIELD)).clear()
        self.driver.find_element(*self.PHONE_FIELD).send_keys(Ph_number)

        self.wait.until(EC.presence_of_element_located(self.ADDRESS_FIELD)).clear()
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)






