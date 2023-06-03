from locators import MainPageLocators, LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import profile_page


class TestNavigateToPersonalAccount:
    def test_to_profile_before_login(self, driver):
        driver.find_element(*MainPageLocators.personal_acc).click()
        login_h2 = driver.find_element(*LoginPageLocators.header).text
        assert login_h2 == 'Вход'

    def test_to_profile_after_login(self, login_user_from_main_page):
        login_user_from_main_page.find_element(*MainPageLocators.personal_acc).click()
        WebDriverWait(login_user_from_main_page, 5).until(expected_conditions.url_to_be(profile_page))
        assert login_user_from_main_page.current_url == profile_page
