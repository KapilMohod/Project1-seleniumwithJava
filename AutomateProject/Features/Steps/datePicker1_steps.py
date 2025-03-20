from behave import *
from pageObject.datePickerPage1 import datePickerPage1

@then('User select the date from date picker1')
def dt_picker_steps(context):
    page = datePickerPage1(context.driver)
    page.select_date_from_datepicker()