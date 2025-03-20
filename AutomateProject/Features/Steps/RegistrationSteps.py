
from behave import *
import sys
import os
from pageObject.registrationPage import registrationPage

@when('User navigates the Registration page')
def navigates_RegPage(context):

    page = registrationPage(context.driver)
    page.navigateToPage()

@then ('User Verified the Title')
def title_Verified(context):
    page = registrationPage(context.driver)
    page.titleVerification()


@then('User Enters registration details: "{name}", "{email}", "{Ph_number}", "{address}"')
def details_name_Email(context, name, email, Ph_number, address  ):

    page = registrationPage(context.driver)
    page.fillRegistrationForm(name, email, Ph_number, address)


