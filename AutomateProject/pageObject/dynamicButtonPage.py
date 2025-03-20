from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class dynamicButtonPage:

    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://testautomationpractice.blogspot.com/"
        self.dynamicButton_locator = (By.XPATH, "//button[contains(text(),'START') or contains(text(),'STOP')]")
        self.wait = WebDriverWait(self.driver, 10)


    def navigateTOPage(self):

        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)

    def click_dynamicButton(self):

        dynamic_button = self.wait.until(EC.element_to_be_clickable((self.dynamicButton_locator)))

        dynamic_button.click()

        self.wait.until(EC.text_to_be_present_in_element(self.dynamicButton_locator, "STOP"))

        # Verify the change
        if dynamic_button.text == "STOP":
            print("Button changed to STOP ✅")
            return True
        else:
            print("Button did not change ❌")
            return False



