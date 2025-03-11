Feature: Verificar la página de contacto de ALTEN

  Scenario: Verificar la carga de la página de contacto
    Given I navigate to "https://www.alten.es/contacto/"
    When the page loads completely
    Then I should see the contact form

  Scenario: Verificar el envío del formulario de contacto con datos válidos
    Given I navigate to "https://www.alten.es/contacto/"
    And I accept the popup conditions
    And I fill in the contact form with valid data
    And I check the "No soy robot" checkbox
    When I submit the contact form
    Then I should see a confirmation message

  Scenario: Verificar el envío del formulario de contacto con datos inválidos
    Given I navigate to "https://www.alten.es/contacto/"
    And I accept the popup conditions
    And I fill in the contact form with invalid data
    And I check the "No soy robot" checkbox
    When I submit the contact form
    Then I should see error messages for the invalid fields
