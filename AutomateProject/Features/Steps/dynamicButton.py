from behave import *
from pageObject.dynamicButtonPage import dynamicButtonPage

@then('User click on dynamic button')
def dynamicButtonstep(context):
    page = dynamicButtonPage(context.driver)
    page.click_dynamicButton()