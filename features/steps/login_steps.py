from behave import given, when, then
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils
from selenium.webdriver.common.by import By

@given('the OrangeHRM login page is displayed')
def step_impl(context):
    context.driver.get(utils.URL)
    context.login_page = LoginPage(context.driver)

@when('the user enters valid username and password')
def step_impl(context):
    context.login_page.enter_username(utils.USERNAME)
    context.login_page.enter_password(utils.PASSWORD)

@when('clicks the login button')
def step_impl(context):
    context.login_page.click_login()

@then('the home page should be displayed')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    # Check for welcome link as an indicator of home page
    assert context.driver.find_element(By.CLASS_NAME, context.home_page.welcome_link_class).is_displayed()

@given('the user is logged in')
def step_impl(context):
    context.driver.get(utils.URL)
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_username(utils.USERNAME)
    context.login_page.enter_password(utils.PASSWORD)
    context.login_page.click_login()
    context.home_page = HomePage(context.driver)

@when('the user clicks the welcome link')
def step_impl(context):
    context.home_page.click_welcome()

@when('clicks the logout link')
def step_impl(context):
    context.home_page.click_logout()

@then('the login page should be displayed')
def step_impl(context):
    # Check for login button as an indicator of login page
    # We need to re-instantiate or reuse the login page object logic, 
    # but since we are on the page, we can just check the element.
    # Or better, use the page object locator.
    login_page = LoginPage(context.driver)
    assert context.driver.find_element(By.XPATH, login_page.login_button_xpath).is_displayed()
