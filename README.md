# Python BDD Automation Project

This project is a Behavior-Driven Development (BDD) test automation framework using Python, Behave, and Selenium.

## Project Structure

The repository is organized as follows:

- **`features/`**: Contains the BDD feature files (`.feature`) and the environment configuration.
    - **`steps/`**: Contains the Python step definitions corresponding to the Gherkin steps in the feature files.
    - **`environment.py`**: Defines hooks (setup/teardown) for Behave, such as initializing the browser driver before scenarios and taking screenshots on failure.
- **`pages/`**: Implements the Page Object Model (POM) design pattern. Each file corresponds to a web page (e.g., `loginPage.py`, `homePage.py`) and contains locators and methods to interact with that page.
- **`utils/`**: Contains utility scripts and constants (e.g., `utils.py` for URL, credentials, and helper functions).
- **`reports/`**: Directory where test reports (like Allure results) are generated.
- **`screenshots/`**: Stores screenshots captured during test failures.
- **`drivers/`**: Directory for browser drivers (though `webdriver-manager` is used to manage them automatically).
- **`BUILD.md`**: Detailed instructions on how to set up the environment and run the tests.
- **`requirements.txt`**: List of Python dependencies required for the project.

## Getting Started

Please refer to [BUILD.md](BUILD.md) for detailed instructions on how to install dependencies and run the tests.
