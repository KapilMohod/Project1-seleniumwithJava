import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class drpdwnPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.CountriesDrpdwn = (By.XPATH, "//select[@id='country']/option")
        self.wait = WebDriverWait(self.driver, 10)

    def navigateToPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def Countriesdrpdwn(self):

        Countries_DrpDwn = self.wait.until(EC.visibility_of_all_elements_located((self.CountriesDrpdwn)))
        print("Total Countries available are : ", len(Countries_DrpDwn))
        sys.stdout.flush()

        for countries in Countries_DrpDwn:

            if countries.text == "India":
                countries.click()
                break