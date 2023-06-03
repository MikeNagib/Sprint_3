from selenium.webdriver.common.by import By


class Locators:
    sauces_header = (By.XPATH, '//span[contains(text(),"Соусы")]')  # таб с Соусы
    filling_header = (By.XPATH, '//span[contains(text(),"Начинки")]')  # таб с Начинки
    rolls_header = (By.XPATH, '//span[contains(text(),"Булки")]')  # таб с Булки
    sauces = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    rolls = (By.XPATH, "//h2[contains(text(),'Булки')]")
    filling = (By.XPATH, "//h2[contains(text(),'Начинки')]")

class RegistrPageLocators:
    username = (By.XPATH, "//input[@name='name']")  # ввод имя пользователя
    password = (By.XPATH, "//input[@name='Пароль']")  # ввод пароля
    registr_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка регистрации
    incorrect_password = (By.XPATH, "//p[text()='Некорректный пароль']")  # поле для проверки неправильного пароля
    button_login = (By.XPATH, "// a[text()='Войти']")  # кнопка для логина


class LoginPageLocators:
    header = (By.XPATH, "//h2[text()='Вход']")  # Вход
    login = By.XPATH, './/label[text()=\'Email\']/following-sibling::input'  # Окно для ввода email
    password = By.XPATH, './/input[@type=\'password\' and @name=\'Пароль\']'  # Окно для ввода пароля
    login_button = By.XPATH, './/button[text()=\'Войти\']'  # Кнопка отсылки данных


class MainPageLocators:
    login_button = (By.XPATH, "// button[text() = 'Войти в аккаунт']")  # кнопка для логина
    personal_acc = By.XPATH, './/p[text()=\'Личный Кабинет\']'  # Кнопка перехода в профиль
    constructor_header = (By.XPATH, "// h1[text()='Соберите бургер']")  # хидер на сборку бургера
    save_button = (By.XPATH, ".//button[text()='Сохранить']")  # кнопка Сохранить на странице /account/profile
    logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип


class PersonalAccountLocators:
    constructor_button = (By.XPATH, "// p[text()='Конструктор']")  # кнопка для перехода в конструктор
    logout_button = By.XPATH, './/button[text()=\'Выход\']'  # кнопка для выхода из аккаунта

