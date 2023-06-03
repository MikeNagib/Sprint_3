import pytest
from data import url_name, login_form, GOOD_LOGIN, GOOD_PASSWORD
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_name)
    yield driver
    driver.quit()


@pytest.fixture()
def login_user_from_main_page(driver):
    driver.get(login_form)

    driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
    driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
    driver.find_element(*LoginPageLocators.login_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_changes(login_form))

    yield driver

