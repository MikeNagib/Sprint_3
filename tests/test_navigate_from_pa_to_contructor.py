from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators
from conftest import GOOD_LOGIN, GOOD_PASSWORD


class TestFromPrivate_room_to_constructor:

    def test_move_by_click_to_constructor(self, driver):  # по клику на «Конструктор»
        driver.implicitly_wait(3)
        driver.find_element(*MainPageLocators.login_button).click()
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        driver.find_element(*PersonalAccountLocators.constructor_button).click()
        constructor_h1 = driver.find_element(*MainPageLocators.constructor_header).text
        assert constructor_h1 == 'Соберите бургер'

    def test_move_by_click_to_logo_with_registration(self, driver):  # по клику на логотип Stellar Burgers
        driver.implicitly_wait(3)
        driver.find_element(*MainPageLocators.login_button).click()
        driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
        driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
        driver.find_element(*LoginPageLocators.login_button).click()
        driver.find_element(*MainPageLocators.logo).click()
        constructor_h2 = driver.find_element(*MainPageLocators.constructor_header).text
        assert constructor_h2 == 'Соберите бургер'

