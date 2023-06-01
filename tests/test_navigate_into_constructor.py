from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


def test_chois_constructor_section_filling_sucsses(login_user_from_main_page):  # Переход по соусам
    driver = login_user_from_main_page
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces)))
    driver.find_element(By.XPATH, sauces).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces_traditional_galactic_sauce)))
    driver.find_element(By.XPATH, sauces_traditional_galactic_sauce).click()

    assert driver.find_element(By.XPATH, galactic_sauce_check).text == 'Соус традиционный галактический'

    driver.quit()


def test_chois_constructor_section_sauce_sucsses(login_user_from_main_page):  # Переход по начинке
    driver = login_user_from_main_page
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, filling).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, fillings_cheese_with_asteroid_mold).click()

    assert driver.find_element(By.XPATH, asteroid_mold_check).text == 'Сыр с астероидной плесенью'

    driver.quit()


def test_chois_constructor_section_roll_sucsses(login_user_from_main_page):  # Переход по булкам
    driver = login_user_from_main_page
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauces)))
    driver.find_element(By.XPATH, sauces).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, rolls)))
    driver.find_element(By.XPATH, rolls).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, filling)))
    driver.find_element(By.XPATH, rolls_crater_roll_n_200i).click()

    assert driver.find_element(By.XPATH, rolls_crater_check).text == 'Краторная булка N-200i'

    driver.quit()

