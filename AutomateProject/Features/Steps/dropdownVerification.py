from behave import *
from pageObject.drpdwnPage import drpdwnPage

@then('User select the country from dropdown')
def DrpDwn(context):

    page = drpdwnPage(context.driver)
    page.Countriesdrpdwn()

