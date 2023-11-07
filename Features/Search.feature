Feature: Search Bar testing

  @completed
  Scenario: Search for a valid product
    Given I got nevigated to home page
    When  I enter the valid product in the search box
    And I click on search button
    Then Valid product should be displayed

  Scenario: Search for an invalid product
    Given I got nevigated to home page
    When  I enter the invalid product in the search box
    And I click on search button
    Then Proper message should be displayed in search results


