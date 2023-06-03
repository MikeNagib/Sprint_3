from conftest import url_name, GOOD_LOGIN, GOOD_PASSWORD
from locators import MainPageLocators, LoginPageLocators, RegistrPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogIn:
    def test_login_from_main_page_use_login_button_true(self, driver):
        driver.get(url_name)
        driver.find_element(*MainPageLocators.login_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.header))
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.personal_acc))
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_main_page_use_personal_account_link_true(self, driver):
        driver.get(url_name)
        driver.find_element(*MainPageLocators.personal_acc).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.header))
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.personal_acc))
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_register_page_use_login_button_true(self, driver):
        driver.get(url_name + 'register')
        driver.find_element(*MainPageLocators.personal_acc).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.header))
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.personal_acc))
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check

    def test_login_from_forgot_password_page_use_login_button_true(self, driver):
        driver.get(url_name + 'forgot-password')
        driver.find_element(*RegistrPageLocators.button_login).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.header))
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.personal_acc))
        to_check = driver.find_element(*MainPageLocators.personal_acc).text
        assert 'Личный Кабинет' == to_check
