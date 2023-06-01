from selenium.webdriver.common.by import By

sauces = '//span[text()="Соусы"]'  # таб с Соусы
sauces_traditional_galactic_sauce = '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[3]'
galactic_sauce_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'
filling = '//span[text()="Начинки"]'  # таб с Начинки
fillings_cheese_with_asteroid_mold = '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[9]'
asteroid_mold_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'
rolls = '//span[text()="Булки"]'  # таб с Булки
rolls_crater_roll_n_200i = '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/img'
rolls_crater_check = '//*[@id="root"]/div/section[1]/div[1]/div/p'


class RegistrPageLocators:
    username = (By.XPATH, "//input[@name='name']")  # ввод имя пользователя
    password = (By.XPATH, "//input[@name='Пароль']")  # ввод пароля
    registr_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка регистрации
    incorrect_password = (By.XPATH, "//p[text()='Некорректный пароль']")  # поле для проверки неправильного пароля
    button_login = (By.XPATH, "// a[text()='Войти']")  # кнопка для логина


class LoginPageLocators:
    header = (By.XPATH, "//h2[text()='Вход']")  # Вход
    login = By.XPATH, './/label[text()=\'Email\']/following-sibling::input'  # ввод email
    password = By.XPATH, './/input[@type=\'password\' and @name=\'Пароль\']'  # ввод пароля
    login_button = By.XPATH, './/button[text()=\'Войти\']'  # Кнопка входа


class MainPageLocators:
    login_button = (By.XPATH, "// button[text() = 'Войти в аккаунт']")  # кнопка для логина
    personal_acc = By.XPATH, './/p[text()=\'Личный Кабинет\']'  # Кнопка перехода в профиль
    constructor_header = (By.XPATH, "// h1[text()='Соберите бургер']")  # хидер на сборку бургера
    save_button = (By.XPATH, ".//button[text()='Сохранить']")  # кнопка Сохранить на странице /account/profile
    logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип


class PersonalAccountLocators:
    constructor_button = (By.XPATH, "// p[text()='Конструктор']")  # кнопка для перехода в конструктор
    logout_button = By.XPATH, './/button[text()=\'Выход\']'  # кнопка для выхода из аккаунта
