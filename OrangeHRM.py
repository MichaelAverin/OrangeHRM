import os
import random
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from dotenv import load_dotenv
load_dotenv()

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# локаторы
USERNAME_FIELD = ("xpath", "//input[@name='username']")
PASSWORD_FIELD = ("xpath", "//input[@name='password']")
LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
ADD_BUTTON = ("xpath", "//div[@class='orangehrm-header-container']/button")
PIM_BUTTON = ("xpath", "//span[text()='PIM']")
FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
ID_FIELD = ("xpath", "(//div[contains(@class, 'oxd-grid-2')])[1]//input")
TOGGLE = ("xpath", "//span[contains(@class, 'oxd-switch-input--active')]")
UN_FIELD = ("xpath", "(//input[@autocomplete='off'])[1]")
PW_FIELD = ("xpath", "(//input[@autocomplete='off'])[2]")
CONFIRM_PW_FIELD = ("xpath", "(//input[@autocomplete='off'])[3]")
SAVE_BUTTON = ("xpath", "//button[@type='submit']")
SUCCESS_FIELD = ("xpath", "//p[text()='Success']")
PROFILE_BUTTON = ("xpath", "//span[@class='oxd-userdropdown-tab']")
LOGOUT_BUTTON = ("xpath", "(//a[@class='oxd-userdropdown-link'])[4]")
MY_INFO = ("xpath", "(//li[@class='oxd-main-menu-item-wrapper']/a)[3]")
CALENDAR = ("xpath", "(//input[@placeholder='yyyy-dd-mm'])[1]")
FIRST_APRIL = ("xpath", "//div[@class='oxd-calendar-date' and text()='1']")
NATIONALITY_SELECT = ("xpath", "(//div[@class='oxd-select-text-input'])[1]")
NS_AMERICAN = ("xpath", "//span[text()='American']")
SAVE_BUTTON_2 = ("xpath", "(//button[@type='submit'])[1]")
PHOTO_BUTTON = ("xpath", "//div[@class='orangehrm-edit-employee-image-wrapper']")
ADD_PHOTO = ("xpath", "//input[@type='file']")
SAVE_BUTTON_3 = ("xpath", "//button[@type='submit']")
MY_INFO_2 = ("xpath", "//p[@class='oxd-userdropdown-name']")
LOGOUT_BUTTON_2 = ("xpath", "(//a[@class='oxd-userdropdown-link'])[4]")
SEARCH_NAME = ("xpath", "(//input[@placeholder='Type for hints...'])[1]")
SEARCH_BUTTON = ("xpath", "//div[@class='oxd-form-actions']//button[@type='submit']")
DELETE_BUTTON = ("xpath", "(//div[@class='oxd-table-cell-actions']//button)[2]")
DELETE_CONFIRM = ("xpath", "(//div[@class='orangehrm-modal-footer']//button)[2]")

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(BASE_URL)

# вход в систему со скрытыми данными
wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(os.environ["LOGIN"])
wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(os.environ["PASSWORD"])
wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

# создание нового пользователя
wait.until(EC.element_to_be_clickable(PIM_BUTTON)).click()
wait.until(EC.element_to_be_clickable(ADD_BUTTON)).click()
wait.until(EC.element_to_be_clickable(FIRST_NAME_FIELD)).send_keys("Ivan")
wait.until(EC.element_to_be_clickable(MIDDLE_NAME_FIELD)).send_keys("Ivanovich")
wait.until(EC.element_to_be_clickable(LAST_NAME_FIELD)).send_keys("Ivanov")
# генерация нового ID пользователя с удалением предыдущего
employeeID = wait.until(element_to_be_clickable(ID_FIELD))
employeeID.send_keys(Keys.COMMAND + "A")
employeeID.send_keys(Keys.DELETE)
employeeID.send_keys(f"{random.randint(0000, 9999)}")
# создание у нового пользователя данных для входа в систему
wait.until(EC.element_to_be_clickable(TOGGLE)).click()
wait.until(EC.element_to_be_clickable(UN_FIELD)).send_keys(os.environ["NEW_LOGIN"])
wait.until(EC.element_to_be_clickable(PW_FIELD)).send_keys(os.environ["NEW_PASSWORD"])
wait.until(EC.element_to_be_clickable(CONFIRM_PW_FIELD)).send_keys(os.environ["NEW_PASSWORD"])
wait.until(EC.element_to_be_clickable(SAVE_BUTTON)).click()
# проверка исчезающего элемента
wait.until(EC.visibility_of_element_located(SUCCESS_FIELD))
# выход из системы
wait.until(EC.element_to_be_clickable(PROFILE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

# вход в систему по данным нового пользователя
wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(os.environ["NEW_LOGIN"])
wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(os.environ["NEW_PASSWORD"])
wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()

# изменение персональных данных пользователя, используя тестирование исчезающих элементов
wait.until(EC.element_to_be_clickable(MY_INFO)).click()
wait.until(EC.element_to_be_clickable(CALENDAR)).click()
wait.until(EC.element_to_be_clickable(FIRST_APRIL)).click()
wait.until(EC.element_to_be_clickable(NATIONALITY_SELECT)).click()
wait.until(EC.element_to_be_clickable(NS_AMERICAN)).click()
wait.until(EC.element_to_be_clickable(SAVE_BUTTON_2)).click()
# загрузка изображения
wait.until(EC.element_to_be_clickable(PHOTO_BUTTON)).click()
wait.until(EC.presence_of_element_located(ADD_PHOTO)).send_keys(f"{os.getcwd()}/PHOTO.jpg")
wait.until(EC.element_to_be_clickable(SAVE_BUTTON_3)).click()
# выход из системы
wait.until(EC.element_to_be_clickable(MY_INFO_2)).click()
wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON_2)).click()

# вход в систему по данным администратора и удаление нового пользователя через поиск в системе и с подтверждением операции
wait.until(EC.element_to_be_clickable(USERNAME_FIELD)).send_keys(os.environ["LOGIN"])
wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(os.environ["PASSWORD"])
wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
wait.until(EC.element_to_be_clickable(PIM_BUTTON)).click()
wait.until(EC.element_to_be_clickable(SEARCH_NAME)).send_keys("Ivan Ivanovich Ivanov")
wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()
wait.until(EC.element_to_be_clickable(DELETE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(DELETE_CONFIRM)).click()