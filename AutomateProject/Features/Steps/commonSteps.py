
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given('User Opens the chrome browser')
def browser_opens(context):

    service = Service("C:/Users/ASUS/PycharmProjects/AutomateProject/Drivers/chromedriver.exe") #"C:/Users/ASUS/PycharmProjects/AutomateProject/Drivers/chromedriver.exe"
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

