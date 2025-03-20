import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class datePickerPage1:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.datepicker_locator = (By.ID, "datepicker")
        self.wait = WebDriverWait(self.driver, 10)

    def navigateToPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def select_date_from_datepicker(self, Date="20", Month="November", Year="2026"):
        dt_picker = self.wait.until(EC.presence_of_element_located((self.datepicker_locator)))
        dt_picker.click()

        while True:
            mth = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-month']"))).text
            yr = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-year']"))).text

            if mth==Month and yr==Year:
                break

            else:
                Next = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Next']")))
                Next.click()

                # Prev = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Prev']")))
                # Prev.click()

        Dates = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")))

        for el in Dates:
            if el.text == Date:
                el.click()
                break