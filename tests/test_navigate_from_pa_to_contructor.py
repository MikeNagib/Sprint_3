from locators import MainPageLocators, PersonalAccountLocators


class TestFromPrivate_room_to_constructor:

    def test_move_by_click_to_constructor(self, login_user_from_main_page):

        login_user_from_main_page.find_element(*PersonalAccountLocators.constructor_button).click()
        constructor_h1 = login_user_from_main_page.find_element(*MainPageLocators.constructor_header).text
        assert constructor_h1 == 'Соберите бургер'

    def test_move_by_click_to_logo_with_registration(self, login_user_from_main_page):

        login_user_from_main_page.find_element(*MainPageLocators.logo).click()
        constructor_h2 = login_user_from_main_page.find_element(*MainPageLocators.constructor_header).text
        assert constructor_h2 == 'Соберите бургер'

