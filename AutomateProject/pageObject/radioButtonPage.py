import sys
import os
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class radioButtonPage:

    def __init__(self, driver):

        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.genderOptions = (By.XPATH, "(//div[@class='form-check form-check-inline']/parent::div)[1]/child::div")


    def navigateToPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def selectGender(self):

        wait = WebDriverWait(self.driver, 10)

        try:
            Gender_options = wait.until(EC.presence_of_all_elements_located((self.genderOptions)))
            print("Total Gender's options : ", len(Gender_options))

            for gender in Gender_options:

                if gender.text == "Male":
                    gender.click()
                    break

        except TimeoutException:
            assert False, "Gender options not found within the timeout"


