Feature: Cart Page Check
  Scenario: User is on the Cart Page
    Given We open the site
    When We verify the cart link and open it
    Then We verify user is on the cart page