from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactoPage(BasePage):
    NOMBRE_INPUT = (By.NAME, 'first_ame')
    APELLIDOS_INPUT = (By.NAME, 'last_name')
    EMAIL_INPUT = (By.NAME, 'email')
    TELEFONO_INPUT = (By.NAME, 'telefphoneono')
    EMPRESA_INPUT = (By.NAME, 'company_name')
    CATEGORIA_SELECT = (By.NAME, 'contact_category')
    MENSAJE_TEXTAREA = (By.NAME, 'message')
    ENVIAR_BUTTON = (By.XPATH, '//*[@id="contact-form"]/div[3]/button')
    NO_SOY_ROBOT_CHECKBOX = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    ACEPTAR_BUTTON = (By.ID, 'tarteaucitronPersonalize2')

    def enter_nombre(self, nombre):
        self.enter_text(self.NOMBRE_INPUT, nombre)

    def enter_apellidos(self, apellidos):
        self.enter_text(self.APELLIDOS_INPUT, apellidos)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_telefono(self, telefono):
        self.enter_text(self.TELEFONO_INPUT, telefono)

    def enter_empresa(self, empresa):
        self.enter_text(self.EMPRESA_INPUT, empresa)

    def select_categoria(self, categoria):
        self.find_element(self.CATEGORIA_SELECT).send_keys(categoria)

    def enter_mensaje(self, mensaje):
        self.enter_text(self.MENSAJE_TEXTAREA, mensaje)

    def click_enviar(self):
        self.click_element(self.ENVIAR_BUTTON)

    def click_no_soy_robot(self):
        self.click_element(self.NO_SOY_ROBOT_CHECKBOX)

    def click_aceptar(self):
        self.click_element(self.ACEPTAR_BUTTON)