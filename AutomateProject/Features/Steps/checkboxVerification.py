from behave import *
from pageObject.checkboxPage import checkboxPage


@then('User Verified the checkboxes')
def checkboxesVerification(context):

    page = checkboxPage(context.driver)
    page.chkBox()




