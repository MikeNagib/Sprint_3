from locators import Locators


class TestNavigateConstructor:
    def test_go_to_sauces_tab(self, driver):
        driver.find_element(*Locators.sauces_header).click()
        login_h2 = driver.find_element(*Locators.sauces).text
        assert login_h2 == 'Соусы'

    def test_go_to_rolls_tab(self, driver):
        driver.find_element(*Locators.rolls_header).click()
        login_h2 = driver.find_element(*Locators.rolls).text
        assert login_h2 == 'Булки'

    def test_go_to_filling_tab(self, driver):
        driver.find_element(*Locators.filling_header).click()
        login_h2 = driver.find_element(*Locators.filling).text
        assert login_h2 == 'Начинки'
