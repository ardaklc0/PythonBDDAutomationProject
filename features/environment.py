from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure
from allure_commons.types import AttachmentType

def before_scenario(context, scenario):
    # Default to chrome, but could be extended to read from userdata or env vars
    # Behave doesn't have a built-in command line option parser for custom args like pytest
    # But we can use userdata.
    
    browser_name = context.config.userdata.get("browser", "chrome")

    if browser_name == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service)
    else:
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)

    context.driver.implicitly_wait(5)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    
    if hasattr(context, 'driver'):
        context.driver.quit()
