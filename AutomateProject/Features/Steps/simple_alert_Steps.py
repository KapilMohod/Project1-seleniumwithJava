from behave import *
from pageObject.simple_alertPage import simple_alertPage

@then('User click on simple alerts and accept it')
def simp_Alert_step(context):
    page = simple_alertPage(context.driver)
    page.acceptSimpleAlert()
