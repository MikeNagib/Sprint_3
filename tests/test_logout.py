from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import login_form, profile_page


class TestNavigateToPersonalAccount:

    def test_logout_by_profile_logout_button(self, login_user_from_main_page):
        login_user_from_main_page.find_element(*MainPageLocators.personal_acc).click()
        WebDriverWait(login_user_from_main_page, 5).until(expected_conditions.url_to_be(profile_page))

        login_user_from_main_page.find_element(*PersonalAccountLocators.logout_button).click()
        WebDriverWait(login_user_from_main_page, 5).until(expected_conditions.url_to_be(login_form))

        login_button = login_user_from_main_page.find_element(*LoginPageLocators.login_button).text
        assert login_button == 'Войти'
