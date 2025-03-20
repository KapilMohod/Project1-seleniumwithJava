from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class simple_alertPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.simpleAlert_locator = (By.ID, "alertBtn")
        self.wait = WebDriverWait(self.driver, 10)


    def navigateTOPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def acceptSimpleAlert(self):

        simpleAlert = self.wait.until(EC.presence_of_element_located((self.simpleAlert_locator)))
        simpleAlert.click()

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()



