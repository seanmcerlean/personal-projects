import sys
sys.path.append('../page_objects')

from behave import *
from page_objects.login_page import LoginPage

@given('I am on the login page')
def I_am_on_the_login_page(context):
    login_page = LoginPage(context.driver)
    login_page.navigate(context.base_url)
    context.current_page = login_page

@when('I enter {username} and {password}')
def I_enter_username_and_password(context, username, password):
    login_page = context.current_page
    login_page.enter_username(username)
    login_page.enter_password(password)

@when('I press the login button')
def I_press_the_login_button(context):
    login_page = context.current_page
    login_page.submit()

@then('I see the message {error_message}')
def I_see_the_message(context, error_message):
    assert error_message in context.driver.page_source
