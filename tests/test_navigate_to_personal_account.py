from locators import MainPageLocators, LoginPageLocators
from conftest import GOOD_LOGIN, GOOD_PASSWORD


class TestNavigateToPersonalAccount:
    def test_to_profile_before_login(self, driver):  # по клику на «Личный кабинет» до авторизации
        driver.implicitly_wait(3)
        driver.find_element(*MainPageLocators.personal_acc).click()
        login_h2 = driver.find_element(*LoginPageLocators.header).text
        assert login_h2 == 'Вход'

    def test_to_profile_after_login(self, driver):  # по клику на «Личный кабинет» после авторизации
        driver.implicitly_wait(3)
        driver.find_element(*MainPageLocators.login_button).click()
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        driver.find_element(*MainPageLocators.personal_acc).click()
        save_button = driver.find_element(*MainPageLocators.save_button).text
        assert save_button == 'Сохранить'

