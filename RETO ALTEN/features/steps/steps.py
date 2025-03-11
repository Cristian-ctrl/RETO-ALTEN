from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.contacto_page import ContactoPage
import os
import logging
import csv
import chromedriver_autoinstaller
from time import sleep

def take_screenshot(context, step_name): 
    context.driver.save_screenshot(f'screenshots/screenshot_{step_name}_{context.scenario.name}.png')

@given('I navigate to "https://www.alten.es/contacto/"')
def step_open_contacto_page(context):
    chromedriver_autoinstaller.install()
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.alten.es/contacto/')
    sleep(10)
    context.contacto_page = ContactoPage(context.driver)
    take_screenshot(context, 'navigate_to_contacto_page')

@when('I accept the popup conditions')
def step_accept_popup(context):
    sleep(10)
    context.contacto_page.click_aceptar()
    take_screenshot(context, 'accept_popup_conditions')

@when('I fill in the contact form with valid data')
def step_fill_contact_form_valid(context):
    sleep(10)
    context.contacto_page.enter_nombre('Cristian')
    context.contacto_page.enter_apellidos('Pérez')
    context.contacto_page.enter_email('cristian@example.com')
    context.contacto_page.enter_telefono('123456789')
    context.contacto_page.enter_empresa('Mi Empresa')
    context.contacto_page.select_categoria('Categoría')
    context.contacto_page.enter_mensaje('Hola, este es un mensaje de prueba.')
    take_screenshot(context, 'fill_contact_form_valid')

@when('I fill in the contact form with invalid data')
def step_fill_contact_form_invalid(context):
    sleep(10)
    context.contacto_page.enter_nombre('')
    context.contacto_page.enter_apellidos('')
    context.contacto_page.enter_email('cristian@')
    context.contacto_page.enter_telefono('abcdefg')
    context.contacto_page.enter_empresa('')
    context.contacto_page.select_categoria('')
    context.contacto_page.enter_mensaje('')
    take_screenshot(context, 'fill_contact_form_invalid')

@when('I check the "No soy robot" checkbox')
def step_check_no_soy_robot(context):
    sleep(10)
    context.contacto_page.click_no_soy_robot()
    take_screenshot(context, 'check_no_soy_robot')

@when('I submit the contact form')
def step_submit_contact_form(context):
    sleep(10)
    context.contacto_page.click_enviar()
    take_screenshot(context, 'submit_contact_form')

@then('I should see a confirmation message')
def step_verify_confirmation(context):
    sleep(10)
    take_screenshot(context, 'verify_confirmation_message')
    context.driver.quit()

@then('I should see error messages for the invalid fields')
def step_verify_error_messages(context):
    sleep(10)
    take_screenshot(context, 'verify_error_messages')
    context.driver.quit()

@then('I should be redirected to the privacy policy page')
def step_verify_privacy_policy(context):
    sleep(10)
    take_screenshot(context, 'verify_privacy_policy')
    context.driver.quit()

logging.basicConfig(filename='logs/test_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_test_result(scenario_name, result, error_description=''):
    with open('reports/test_report.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([scenario_name, result, error_description])
