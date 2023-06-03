from data import url_name, USER_NAME, BAD_PASSWORD
from helper import generate_login, generate_password
from locators import RegistrPageLocators, LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    def test_register_new_user(self, driver):
        driver.get(url_name + 'register')
        driver.find_elements(*RegistrPageLocators.username)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrPageLocators.username)[1].send_keys(generate_login())
        driver.find_element(*RegistrPageLocators.password).send_keys(generate_password())
        driver.find_element(*RegistrPageLocators.registr_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.header))
        current_url = driver.current_url
        assert current_url == url_name + 'login'

    def test_register_new_user_with_bad_password_false(self, driver):
        driver.get(url_name + 'register')
        driver.find_elements(*RegistrPageLocators.username)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrPageLocators.username)[1].send_keys(generate_login())
        driver.find_element(*RegistrPageLocators.password).send_keys(BAD_PASSWORD)
        driver.find_element(*RegistrPageLocators.registr_button).click()
        response = driver.find_element(*RegistrPageLocators.incorrect_password).text
        assert 'Некорректный пароль' == response
