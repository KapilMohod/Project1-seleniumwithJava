import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class checkboxPage:

    def __init__(self, driver):

        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.selectChkBox = (By.XPATH, "(//div[@class='form-check form-check-inline']/parent::div)[2]/child::div")
        self.wait = WebDriverWait(self.driver, 10)

    def navigateToPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def chkBox(self):

        Days = self.wait.until(EC.presence_of_all_elements_located((self.selectChkBox)))
        print("Total days counts : ", len(Days))

        for day in Days:
            print("The day is : ", day.text)

            if day.text in ["Monday", "Friday"]:

                try:
                    # Find and click the checkbox inside the div
                    checkbox = day.find_element(By.TAG_NAME, "input")
                    if not checkbox.is_selected():  # Ensure it's not already selected
                        checkbox.click()
                except Exception as e:
                    print(f"Error clicking checkbox for {day.text}: {e}")
