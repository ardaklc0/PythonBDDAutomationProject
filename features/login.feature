Feature: Login and Logout
  As a user
  I want to login and logout of the OrangeHRM application

  Scenario: Valid Login
    Given the OrangeHRM login page is displayed
    When the user enters valid username and password
    And clicks the login button
    Then the home page should be displayed

  Scenario: Valid Logout
    Given the user is logged in
    When the user clicks the welcome link
    And clicks the logout link
    Then the login page should be displayed
