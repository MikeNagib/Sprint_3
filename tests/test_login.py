from conftest import url_name, GOOD_LOGIN, GOOD_PASSWORD
from locators import MainPageLocators, LoginPageLocators, RegistrPageLocators
from conftest import webdriver_wait


class TestLogIn:
    def test_login_from_main_page_use_login_button_true(self, driver):  # вход по кнопке «Войти в аккаунт» на главной
        driver.get(url_name)
        driver.find_element(*MainPageLocators.login_button).click()
        webdriver_wait(driver, LoginPageLocators.header)
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        webdriver_wait(driver, MainPageLocators.personal_acc)
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_main_page_use_personal_account_link_true(self, driver):  # вход через кнопку «Личный кабинет»
        driver.get(url_name)
        driver.find_element(*MainPageLocators.personal_acc).click()
        webdriver_wait(driver, LoginPageLocators.header)
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        webdriver_wait(driver, MainPageLocators.personal_acc)
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_register_page_use_login_button_true(self, driver):  # вход через кнопку в форме регистрации,
        driver.get(url_name + 'register')
        driver.find_element(*MainPageLocators.personal_acc).click()
        webdriver_wait(driver, LoginPageLocators.header)
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        webdriver_wait(driver, MainPageLocators.personal_acc)
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_forgot_password_page_use_login_button_true(self, driver):  # вход в форме восстановления пароля
        driver.get(url_name + 'forgot-password')
        driver.find_element(*RegistrPageLocators.button_login).click()
        webdriver_wait(driver, LoginPageLocators.header)
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        webdriver_wait(driver, MainPageLocators.personal_acc)
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

