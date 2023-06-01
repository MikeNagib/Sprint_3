from conftest import url_name, generate_login, generate_password, USER_NAME, BAD_PASSWORD
from conftest import webdriver_wait
from locators import RegistrPageLocators, LoginPageLocators


class TestRegistration:
    def test_register_new_user(self, driver):  # Успешная регистрация
        driver.get(url_name + 'register')
        driver.find_elements(*RegistrPageLocators.username)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrPageLocators.username)[1].send_keys(generate_login())
        driver.find_element(*RegistrPageLocators.password).send_keys(generate_password())
        driver.find_element(*RegistrPageLocators.registr_button).click()
        webdriver_wait(driver, LoginPageLocators.header)
        current_url = driver.current_url
        assert current_url == url_name + 'login'

    def test_register_new_user_with_bad_password_false(self, driver):  # Ошибкa для некорректного пароля
        driver.get(url_name + 'register')
        driver.find_elements(*RegistrPageLocators.username)[0].send_keys(USER_NAME)
        driver.find_elements(*RegistrPageLocators.username)[1].send_keys(generate_login())
        driver.find_element(*RegistrPageLocators.password).send_keys(BAD_PASSWORD)
        driver.find_element(*RegistrPageLocators.registr_button).click()
        response = driver.find_element(*RegistrPageLocators.incorrect_password).text
        assert 'Некорректный пароль' == response

