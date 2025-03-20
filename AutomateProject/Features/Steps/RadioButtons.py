import sys
import os
from behave import *
from pageObject.radioButtonPage import radioButtonPage

@then('User select the gender')
def selectGender(context):

    page = radioButtonPage(context.driver)
    page.selectGender()

