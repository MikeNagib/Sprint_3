import pytest
import random

from random import randint
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators
from selenium.webdriver.common.by import By

url_name = "https://stellarburgers.nomoreparties.site/"
USER_NAME = "MihailNagibin"
BAD_PASSWORD = "1234"
COGORTA_ID = "10"
EMAIL_DOMAIN = "yandex.ru"
EMAIL_USER = "mike315414"
GOOD_LOGIN = "mike315414@yandex.ru"
GOOD_PASSWORD = "QW__12"
TIME_TO_WAIT_ELEMENTS = 3
button1 = '//button[text()="Войти в аккаунт"]'
button2 = '//button[text()="Войти"]'


def generate_login():  # генерирует логины
    return EMAIL_USER + COGORTA_ID + str(randint(000, 999)) + "@" + EMAIL_DOMAIN


def generate_password():  # генерирует пароли
    password = random.randint(1000001, 9999999)
    return password


def webdriver_wait(driver_to_use, locator):
    WebDriverWait(driver_to_use, TIME_TO_WAIT_ELEMENTS).until(
        expected_conditions.visibility_of_element_located(locator))


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_name)
    yield driver
    driver.quit()


@pytest.fixture()  # авторизация
def login_user_from_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_name)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, button1)))
    driver.find_element(By.XPATH, button1).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, button2)))
    driver.find_element(*LoginPageLocators.login).send_keys(GOOD_LOGIN)
    driver.find_element(*LoginPageLocators.password).send_keys(GOOD_PASSWORD)
    driver.find_element(By.XPATH, button2).click()
    return driver

