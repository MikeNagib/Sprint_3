from conftest import GOOD_LOGIN, GOOD_PASSWORD
from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators


class TestNavigateToPersonalAccount:

    def test_logout_by_profile_logout_button(self, driver):  # Выход из Личного кабинета
        driver.implicitly_wait(3)
        driver.find_element(*MainPageLocators.login_button).click()
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        driver.find_element(*MainPageLocators.personal_acc).click()
        driver.find_element(*PersonalAccountLocators.logout_button).click()
        login_button = driver.find_element(*LoginPageLocators.login_button).text
        assert login_button == 'Войти'

